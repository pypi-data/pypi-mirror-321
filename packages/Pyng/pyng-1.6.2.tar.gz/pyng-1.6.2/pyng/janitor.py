#!/usr/bin/python
"""\
@file   janitor.py
@author Nat Goodspeed
@date   2011-09-14
@brief  Janitor class to clean up arbitrary resources

Copyright (c) 2011, Nat Goodspeed
"""

import atexit
from collections import namedtuple
from functools import partial
import itertools
from pyng.exc import describe
import sys

class Error(Exception):
    pass

class _Dummy(object):
    """
    No-op file-like output-only object that discards everything written.
    """
    def write(self, data):
        pass

    def flush(self):
        pass

class Janitor(object):
    """
    Janitor provides a uniform way to deal with the possibility of exceptions
    in a function that acquires more and more temporary resources as it
    proceeds. While it's possible to structure such a function as:

    first = acquire()
    try:
        # ...
        second = acquire()
        try:
            # ...
            third = acquire()
            try:
                # ...
            finally:
                third.release()
        finally:
            second.release()
    finally:
        first.release()

    the extra indentation obscures the business logic, and (given finite
    screen width) makes it harder to read later code passages.

    Janitor 'flattens' the logic:

    with Janitor() as janitor:
        first = acquire()
        janitor.cleanup(first.release)
        # ...
        second = acquire()
        janitor.cleanup(second.release)
        # ...
        third = acquire()
        janitor.cleanup(third.release)
        # ...

    An exception that occurs anywhere in the body of the 'with' block will
    cause that Janitor instance to clean up exactly the resources that have
    been acquired to that point. On successful completion of the 'with' block,
    all temporary resources are cleaned up.

    Resources are cleaned up in reverse order of acquisition, just as in the
    try/finally nesting illustrated above.

    Moreover, Janitor also supports atomicity. A function that must produce
    multiple side effects if successful -- or none at all on failure -- can
    use Janitor as follows:

    with Janitor() as janitor:
        first = create()
        janitor.rollback(first.destroy)
        # ...
        second = create()
        janitor.rollback(second.destroy)
        # ...

    If the second create() (or anything after janitor.rollback(first.destroy))
    raises an exception, first.destroy() is called, and so forth.

    cleanup() and rollback() calls may be intermingled. An action passed to
    cleanup() is performed unconditionally; an action passed to rollback() is
    performed only on exception. The appropriate actions are still performed
    in strict reverse order:

    with Janitor() as janitor:
        janitor.cleanup(print, 'first')
        janitor.rollback(print, 'second')
        janitor.cleanup(print, 'third')
        raise RuntimeError('stop')

    prints:

    third
    second
    first

    Without the exception:

    with Janitor() as janitor:
        janitor.cleanup(print, 'first')
        janitor.rollback(print, 'second')
        janitor.cleanup(print, 'third')

    prints:

    third
    first

    Usage:

    Context Manager:
    with Janitor(sys.stdout) as janitor: # report cleanup actions on stdout
        ...
        janitor.cleanup(shutil.rmtree, some_temp_directory)
        ...
        janitor.rollback(os.remove, candidatefile)
        ...
    # exiting 'with' block normally performs cleanup() actions;
    # exiting with an exception performs cleanup() and rollback() actions

    Passing a file-like output stream to Janitor's constructor causes it to
    report its actions to that stream.

    Passing a _desc='description string' keyword parameter to either cleanup()
    or rollback() causes Janitor to report the operation in question using
    that 'description string'. Otherwise it attempts to deduce the function
    name. The underscore on _desc is to permit passing a desc= keyword
    parameter to a cleanup action.

    A Janitor instance is reusable. Thus it may be stored as an instance
    attribute of a class object and shared among methods of that class; the
    top-level entry point can write 'with self.janitor:' and control the final
    cleanup.

    Moreover, the same Janitor instance (e.g. an instance attribute) may be
    reused in nested 'with' statements (e.g. in that object's methods).
    Exiting each 'with' block only performs cleanup actions (whether cleanup()
    or rollback()) registered within or below that 'with' block, according to
    how that particular 'with' block is exited.

    Test Class:
    class TestMySoftware(unittest.TestCase, Janitor):
        def __init__(self):
            Janitor.__init__(self)  # quiet cleanup
            ...

        def setUp(self):
            ...
            self.cleanup(os.rename, saved_file, original_location)
            ...

        def tearDown(self):
            Janitor.tearDown(self)  # calls done()
            ...
            # Or, if you have no other tearDown() logic for
            # TestMySoftware, you can omit the TestMySoftware.tearDown()
            # def entirely and let it inherit Janitor.tearDown().

    For pytest, Janitor also provides teardown_method() that calls done().

    Note that outside a 'with' block, Janitor cannot distinguish between
    successful completion and exception -- so in that case it does not honor
    rollback(). In fact, calling rollback() on a Janitor instance not used as
    a context manager raises Error. This is deemed safer than silently
    ignoring rollback() calls.
    """
    # always: True for cleanup(), False for rollback()
    # desc:   description to be reported on `report` stream
    # func:   callable(type, value, tb) that calls caller's action.
    # For cleanup() and rollback(), `func` ignores (type, value, tb): consumer
    # doesn't want to have to code their passed func to accept them. Only for
    # context() are those parameters significant.
    triple = namedtuple('triple', ('always', 'desc', 'func'))
    
    def __init__(self, report=None, errors=sys.stderr):
        """
        If you pass report= (e.g.) sys.stdout or sys.stderr, Janitor will
        report its cleanup operations as it performs them. If you don't, it
        will perform them quietly -- unless one or more of the actions throws
        an exception, in which case you'll get output on the stream passed as
        errors.
        """
        self.report  = report or _Dummy()
        self.errors  = errors
        self.actions = []
        self.with_depth = []

    def cleanup(self, func, *args, **kwds):
        """
        Unconditionally call func(*args, **kwds) at done() time.

        Pass the callable you want to call at done() time, plus any
        positional or keyword args you want to pass it.

        Pass keyword-only _desc='description' to describe the cleanup action
        as 'description' instead of as 'func(args, kwds)'.
        """
        self._add(True, func, *args, **kwds)

    def rollback(self, func, *args, **kwds):
        """
        Call func(*args, **kwds) only if we leave with an exception.

        Pass keyword-only _desc='description' to describe the cleanup action
        as 'description' instead of as 'func(args, kwds)'.

        Calling this outside a 'with' block raises Error.
        """
        if not self.with_depth:
            raise Error("Calling Janitor.rollback() outside a 'with' block is an error")

        self._add(False, func, *args, **kwds)

    def context(self, manager):
        """
        Immediately call context manager's `__enter__()`, returning its `as`.
        At done() time, call its `__exit__()`.

        So instead of:

        with Janitor(sys.stdout) as janitor:
            # ... some preliminary setup that might require cleanup ...
            with MyContextManager() as mgr:
                # ... actual business logic ...

        you can write:

        with Janitor(sys.stdout) as janitor:
            # ... some preliminary setup that might require cleanup ...
            mgr = janitor.context(MyContextManager())
            # ... actual business logic ...

        It's Janitor's usual value proposition: flattening nested blocks.
        """
        # Avoid _add(), which stores a `func` that explicitly ignores its
        # three arguments. For manager.__exit__(), we WANT to forward those
        # arguments.
        self.actions.append(
            self.triple(
                always=True,
                desc=self._name_for(manager) + '.__exit__()',
                func=manager.__exit__))
        return manager.__enter__()

    def atexit(self):
        """
        Arrange to call done() before normal script termination.
        """
        atexit.register(self.done)

    def _add(self, always, func, *args, **kwds):
        # Support a keyword-only desc= parameter for both cleanup() and rollback()
        try:
            desc = kwds.pop('_desc')
        except KeyError:
            # Caller didn't pass _desc= keyword parameter.
            name = self._name_for(func)
            # Construct a description of this operation in Python syntax from
            # args, kwds.
            desc = "{}({})".format(name, ", ".join(itertools.chain((repr(a) for a in args),
                                                                   (u"{}={!r}".format(k, v)
                                                                    for (k, v) in kwds.items()))))

        # Use functools.partial() to bind passed args and keywords to the
        # passed func so we get a trinary callable (as documented for
        # `triple`) that ignores its three args and does what caller wants.
        self.actions.append(
            self.triple(
                always=always,
                desc=desc,
                func=lambda type, value, tb: partial(func, *args, **kwds)))

    def _name_for(self, obj):
        # Get a name string for 'obj'.
        try:
            # A free function has a __name__
            return obj.__name__
        except AttributeError:
            try:
                # A class object (even builtin objects like ints!) support
                # __class__.__name__
                return obj.__class__.__name__
            except AttributeError:
                # Shrug! Just use repr() to get a string describing this obj.
                return repr(obj)

    def __enter__(self):
        # remember how many actions were already in our list at entry to this
        # 'with' block
        self.with_depth.append(len(self.actions))
        return self

    def __exit__(self, type, value, tb):
        # recall how many pre-existing actions were on our list at entry to
        # this level of 'with' block; only perform what we've added since then
        backto = self.with_depth.pop(-1)
        # Perform cleanup no matter how we exit this 'with' statement.
        # Pass (type, value, tb) to any context manager __exit__() methods
        # registered by context().
        self._call_some(type, value, tb, backto=backto)
        # Propagate any exception from the 'with' statement, don't swallow it
        return False

    def done(self):
        """
        Perform all the actions saved with cleanup() calls.
        Ignore rollback() actions: calling done() states you were successful.
        """
        self._call_some(None, None, None, backto=0)

    def _call_some(self, type, value, tb, backto):
        """
        Perform all the actions saved with cleanup() calls (since backto).
        If type is not None, perform rollback() actions along the way too.
        """
        # Are we exiting a `with` block due to exception?
        exc = type is not None
        # Snip off the tail of self.actions added since backto.
        actions = self.actions[backto:]
        del self.actions[backto:]
        # Typically one allocates resource A, then allocates resource B that
        # depends on it. In such a scenario it's appropriate to delete B
        # before A -- so perform cleanup actions in reverse order. (This is
        # the same strategy used by atexit().)
        while actions:
            # Until our list is empty, pop the last triple.
            triple = actions.pop(-1)

            # cleanup() actions are always performed.
            # rollback() actions are performed only when we hit an exception.
            if not (triple.always or exc):
                continue

            # If requested, report the action.
            print(triple.desc, file=self.report)

            try:
                # Call the bound callable, passing __exit__() arguments in
                # case this triple is a manager.__exit__() function registered
                # by context().
                triple.func(type, value, tb)
            except Exception as err:
                # This is cleanup. Report the problem but continue.
                print("Calling {}\nraised  {}".format(triple.desc, describe(err)),
                      file=self.errors)

    def tearDown(self):
        """
        If a unittest.TestCase subclass (or a nose test class) adds Janitor as
        one of its base classes, and has no other tearDown() logic, let it
        inherit Janitor.tearDown().
        """
        self.done()

    def teardown_method(self, method):
        """
        If a pytest class adds Janitor as one of its base classes, and has no
        other teardown_method() logic, let it inherit this teardown_method().
        """
        self.done()
