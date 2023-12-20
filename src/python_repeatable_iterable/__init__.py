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
from typing import Iterable, NewType, Type
from _collections_abc import dict_keys, dict_values, dict_items
from python_none_objects import NoneIterable


RepeatableIterable = NewType("RepeatableIterable", Iterable)


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
