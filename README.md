# python-repeatable-iterable

[![pypi-version]][pypi]
[![Downloads](https://img.shields.io/pypi/dm/python-repeatable-iterable)](https://pypistats.org/packages/python-repeatable-iterable)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![CodeFactor](https://www.codefactor.io/repository/github/llyaudet/python-repeatable-iterable/badge/main)](https://www.codefactor.io/repository/github/llyaudet/python-repeatable-iterable/overview/main)
[![CodeClimateMaintainability](https://api.codeclimate.com/v1/badges/89044bfd52999e4f07f6/maintainability)](https://codeclimate.com/github/LLyaudet/python-repeatable-iterable/maintainability)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1c70116c2d714e3889606519937cb11d)](https://app.codacy.com/gh/LLyaudet/python-repeatable-iterable/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
![GitHub top language](https://img.shields.io/github/languages/top/llyaudet/python-repeatable-iterable)
![GitHub License](https://img.shields.io/github/license/llyaudet/python-repeatable-iterable)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-repeatable-iterable)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/llyaudet/python-repeatable-iterable)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/LLyaudet)](https://github.com/sponsors/LLyaudet)

|     **A new type RepeatableIterable for Python and a way to obtain one instance**     |

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
from python_repeatable_iterable import RepeatableIterable

def foo(iterable: RepeatableIterable[object]):
    for that in iterable:
        bar(that)
    for that in iterable:
        baz(that)

something_else = RepeatableIterable(something)
foo(something_else)
```

After solution 2:
```python3
from python_repeatable_iterable import RepeatableIterable

def foo(iterable: Iterable):
    iterable = RepeatableIterable(iterable)
    for that in iterable:
        bar(that)
    for that in iterable:
        baz(that)

foo(something)
```

If you develop something where you have no control on what another dev might give you as input,
you have 2 possibilities:

- hope for the best ;),
- or harden your code to have less support work to do :).

This applies if you dev something that is:

- closed source or open source,
- available to everyone on the Internet,
  available only to customers or colleagues that you may personally know or not.

Solution 2 above is a nice solution with a reasonable performance cost :).

[pypi-version]: https://img.shields.io/pypi/v/python-repeatable-iterable.svg
[pypi]: https://pypi.org/project/python-repeatable-iterable/
