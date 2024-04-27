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

echo "Building README.md"
./build_readme.sh

echo "Running isort"
isort .

echo "Running black"
black .

echo "Running pylint"
pylint src/python_repeatable_iterable/

echo "Running mypy"
mypy .

shopt -s globstar

too_long_code_lines() {
  grep -r '.\{71\}' -- **/*.c
  grep -r '.\{71\}' -- **/*.css
  grep -r '.\{71\}' -- **/*.h
  grep -r '.\{71\}' -- **/*.htm
  grep -r '.\{71\}' -- **/*.html
  grep -r '.\{71\}' -- **/*.js
  grep -r '.\{71\}' -- **/*.json
  grep -r '.\{71\}' -- **/*.md
  grep -r '.\{71\}' -- **/*.php
  grep -r '.\{71\}' -- **/*.py
  grep -r '.\{71\}' -- **/*.sql
  grep -r '.\{71\}' -- **/*.tex
  grep -r '.\{71\}' -- **/*.toml
  grep -r '.\{71\}' -- **/*.ts
  grep -r '.\{71\}' -- **/*.txt
  grep -r '.\{71\}' -- **/*.yml
  grep -r '.\{71\}' -- **/COPYING
  grep -r '.\{71\}' -- **/COPYING.LESSER
}

echo "Analyzing too long lines"
too_long_code_lines

