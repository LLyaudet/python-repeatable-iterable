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

©Copyright 2023-2024 Laurent Lyaudet
"""

import sys
from typing import Iterable, List, Never, TypeVar

sys.path.insert(0, "../src/")
# pylint: disable-next=wrong-import-position
from python_repeatable_iterable import RepeatableIterable

# pylint: disable-next=invalid-name
T1 = TypeVar("T1")


def test_arg_to_return_typing(
    x: RepeatableIterable[List[T1]],
) -> List[T1]:
    """
    Check that mypy follows the types
    between the argument and the return of the function
    for the type of the content of the list.
    """
    result = []
    for y in x:
        result.extend(y)
    for y in x:
        result.extend(y)
    return result


def test_arg_to_return_via_call_typing(
    x: Iterable[List[T1]],
) -> List[T1]:
    """
    Check that mypy follows the types
    between the argument and the return of the function
    for the type of the content of the list
    with indirections.
    """
    return test_arg_to_return_typing(RepeatableIterable(x))


a: List[List[Never]] = [[], []]
print(test_arg_to_return_via_call_typing(a))

b = (x for x in a)
print(test_arg_to_return_via_call_typing(b))


def test_arg_to_return_via_cast_typing(
    x: RepeatableIterable[List[T1]],
) -> RepeatableIterable[T1]:
    """
    Check that mypy follows the types
    between the argument and the return of the function
    for the type of the content of the list
    with a final cast.
    """
    result = []
    for y in x:
        result.extend(y)
    for y in x:
        result.extend(y)
    return RepeatableIterable(result)
