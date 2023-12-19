# python-repeatable-iterable

[![pypi-version]][pypi]

**A new type RepeatableIterable for Python and a way to obtain one instance**

Since in Python an Iterator is an Iterable and that you cannot iterate multiple times on an iterator,
you may encounter WTF bugs, even with type checking.
This package provides possible solutions to this problem.
See here for a discussion on this problem:
<https://stackoverflow.com/questions/63104689/what-is-the-pythonic-way-to-represent-an-iterable-that-can-be-iterated-over-mult>

Before:
```python3
def foo(iterable: Iterable):
    for that in iterable:
        bar(that)
    for that in iterable:
        # possible bug
        baz(that)

foo(something)
```

After solution 1:
```python3
from python_repeatable_iterable import RepeatableIterable, get_repeatable_iterable

def foo(iterable: RepeatableIterable):
    for that in iterable:
        bar(that)
    for that in iterable:
        baz(that)

something_else = get_repeatable_iterable(something)
foo(something_else)
```

After solution 2:
```python3
from python_repeatable_iterable import get_repeatable_iterable

def foo(iterable: Iterable):
    iterable = get_repeatable_iterable(iterable)
    for that in iterable:
        bar(that)
    for that in iterable:
        baz(that)

foo(something)
```

[pypi-version]: https://img.shields.io/pypi/v/python-repeatable-iterable.svg
[pypi]: https://pypi.org/project/python-repeatable-iterable/
