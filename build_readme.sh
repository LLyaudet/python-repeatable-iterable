#!/bin/bash
# This file is part of python-repeatable-iterable library.
#
# python-repeatable-iterable is free software:
# you can redistribute it and/or modify it under the terms
# of the GNU Lesser General Public License
# as published by the Free Software Foundation,
# either version 3 of the License,
# or (at your option) any later version.
#
# python-repeatable-iterable is distributed in the hope
# that it will be useful,
# but WITHOUT ANY WARRANTY;
# without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of
# the GNU Lesser General Public License
# along with python-repeatable-iterable.
# If not, see <http://www.gnu.org/licenses/>.
#
# ©Copyright 2023-2024 Laurent Lyaudet

sed -Ez 's/(\[[a-zA-Z0-9:-]*\]: [^\n\\]*)\\\n/\1/Mg'\
  README_printable.md > README_temp.md
sed -Ez 's/(\[[a-zA-Z0-9:-]*\]: [^\n\\]*)\\\n/\1/Mg'\
  README_temp.md > README.md
rm -f README_temp.md

