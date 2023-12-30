"""
This file is part of python-repeatable-iterable library.

python-repeatable-iterable is free software:
you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License
as published by the Free Software Foundation,
either version 3 of the License,
or (at your option) any later version.

python-repeatable-iterable is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with python-repeatable-iterable.
If not, see <http://www.gnu.org/licenses/>.

©Copyright 2023 Laurent Lyaudet
"""
import sys
from typing import Iterable, List, Never, TypeVar

sys.path.insert(0, "../src/")
from python_repeatable_iterable import RepeatableIterable


T1 = TypeVar("T1")


def foo(x: RepeatableIterable[List[T1]]) -> List[T1]:
    result = []
    for y in x:
        result.extend(y)
    for y in x:
        result.extend(y)
    return result


def bar(x: Iterable[List[T1]]) -> List[T1]:
    return foo(RepeatableIterable(x))


a: List[List[Never]] = [[], []]
print(bar(a))

b = (x for x in a)
print(bar(b))


def baz(x: RepeatableIterable[List[T1]]) -> RepeatableIterable[T1]:
    result = []
    for y in x:
        result.extend(y)
    for y in x:
        result.extend(y)
    return RepeatableIterable(result)
