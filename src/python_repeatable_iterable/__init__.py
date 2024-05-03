"""
This file is part of python-repeatable-iterable library.

python-repeatable-iterable is free software:
you can redistribute it and/or modify it under the terms
of the GNU Lesser General Public License
as published by the Free Software Foundation,
either version 3 of the License,
or (at your option) any later version.

python-repeatable-iterable is distributed in the hope
that it will be useful,
but WITHOUT ANY WARRANTY;
without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU Lesser General Public License for more details.

You should have received a copy of
the GNU Lesser General Public License
along with python-repeatable-iterable.
If not, see <http://www.gnu.org/licenses/>.

©Copyright 2023-2024 Laurent Lyaudet
----------------------------------------------------------------------
from typing import Iterable, NewType, Type
from _collections_abc import dict_keys, dict_values, dict_items
from python_none_objects import NoneIterable

A first attempt at defining the RepeatableIterable type,
but it is not generic.
It defines a RepeatableIterable() function that cannot be subscripted.
RepeatableIterable = NewType("RepeatableIterable", Iterable)

----------------------------------------------------------------------

The following function is a first attempt
that conveys the intent more clearly.
But it is not safe, see discussion just after.
def get_repeatable_iterable(
    iterable: Iterable,
    safe_classes: Iterable[Type] = NoneIterable,
) -> RepeatableIterable:
    if isinstance(
        iterable,
        (
            list,
            tuple,
            range,
            str,
            bytes,
            bytearray,
            memoryview,
            set,
            frozenset,
            dict,
            dict_keys,
            dict_values,
            dict_items,
        ),
    ):
        return iterable
    if isinstance(iterable, safe_classes):
        return iterable
    return list(iterable)

Indeed this function is not safe, since you can subclass builtins
or other classes to make them not RepeatableIterable
from the point of view of the semantic of this type.
Consider the following code for example:
>>> class MySet(set):
...     def __init__(self, *args, **kwargs):
...         super().__init__(*args, **kwargs)
...         self.iteration_count = 0
...     def __iter__(self):
...         self.iteration_count += 1
...         if self.iteration_count == 1:
...             return super().__iter__()
...         return ().__iter__()
... 
>>> s = MySet('abcd')
>>> for x in s: print(x)
... 
b
a
d
c
>>> for x in s: print(x)
... 
>>> for x in s: print(x)
... 
>>> isinstance(s, set)
True

See here a list of builtins that can be subclassed or not:
https://stackoverflow.com/questions/10061752
/which-classes-cannot-be-subclassed

----------------------------------------------------------------------

This second attempt has been included in the class RepeatableIterable.
def get_repeatable_iterable(
    iterable: Iterable,
    safe_classes: Iterable[Type] = NoneIterable,
) -> RepeatableIterable:
    # Here is an implementation avoiding the previous problem.
    iterable_type = type(iterable)
    for some_class in (
        list,
        tuple,
        range,
        str,
        bytes,
        bytearray,
        memoryview,
        set,
        frozenset,
        dict,
        dict_keys,
        dict_values,
        dict_items,
        *safe_classes,
    ):
        if iterable_type is some_class:
            return iterable
    return list(iterable)
"""

from typing import Iterable, Iterator, TypeVar, cast
from _collections_abc import dict_items, dict_keys, dict_values

from python_none_objects import NoneIterable

T = TypeVar("T")


class RepeatableIterable(Iterable[T]):
    """
    An asbtract class that is here to define a type and
    cast other objects to this type if possible in its __new__ method.
    """

    # pylint: disable-next=non-iterator-returned
    def __iter__(self) -> Iterator[T]:
        # Instances of RepeatableIterable don't actually exist.
        return NotImplemented

    def __new__(
        cls,
        iterable: Iterable[T],
        safe_classes: Iterable[type[object]] = NoneIterable,
    ) -> "RepeatableIterable[T]":
        """
        Here is an implementation avoiding the previous problem.
        """
        iterable_type = type(iterable)
        for some_class in (
            list,
            tuple,
            range,
            str,
            bytes,
            bytearray,
            memoryview,
            set,
            frozenset,
            dict,
            dict_keys,
            dict_values,
            dict_items,
            *safe_classes,
        ):
            if iterable_type is some_class:
                return cast("RepeatableIterable[T]", iterable)
        return cast("RepeatableIterable[T]", list(iterable))
