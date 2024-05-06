%!/usr/bin/env bash
% This file is part of python-repeatable-iterable library.
%
% python-repeatable-iterable is free software:
% you can redistribute it and/or modify it under the terms
% of the GNU Lesser General Public License
% as published by the Free Software Foundation,
% either version 3 of the License,
% or (at your option) any later version.
%
% python-repeatable-iterable is distributed in the hope
% that it will be useful,
% but WITHOUT ANY WARRANTY;
% without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
% See the GNU Lesser General Public License for more details.
%
% You should have received a copy of
% the GNU Lesser General Public License
% along with python-repeatable-iterable.
% If not, see <https://www.gnu.org/licenses/>.
%
% ©Copyright 2023-2024 Laurent Lyaudet

\documentclass{article}

\usepackage[utf8]{inputenc}
\usepackage{subfigure}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage[pdftex]{hyperref}
\usepackage{tikz}
\usepackage{caption}
\usepackage[round]{natbib}
\usepackage{fancyhdr}
\usepackage{amsfonts}
\usepackage{times}
\usepackage{ifpdf}
\usepackage{latexsym}
\usepackage{graphicx}
\usepackage{enumerate}
\usepackage{pmboxdraw}
\usepackage{fancyvrb}

% *** les environnements ***
%\theoremstyle{break}
\newtheorem{definition}{Definition}[section]
\newtheorem{proposition}[definition]{Proposition}
\newtheorem{theorem}[definition]{Theorem}
\newtheorem{lemma}[definition]{Lemma}
\newtheorem{corollary}[definition]{Corollary}
\newtheorem{remark}[definition]{Remark}
\newtheorem{openproblem}[definition]{Open problem}

\begin{document}

\author{
  Laurent Lyaudet\\
  \url{https://lyaudet.eu/laurent/}\\
  laurent.lyaudet@gmail.com
}
\title{python-repeatable-iterable}

\maketitle
\begin{abstract}
A new type RepeatableIterable for Python
and a way to obtain one instance
\end{abstract}

Current version: @current_date@

Current number of commits: @number_of_commits@

Current git SHA1: @current_git_SHA1@

Code lines: @number_of_lines@

\section{Files tree}
\label{section:tree}

\begin{verbatim}
@current_tree_light@
\end{verbatim}

\begin{verbatim}
@current_tree@
\end{verbatim}

\section{Listing of files}
\label{section:listing}

The following source code is covered by LGPLv3+.
The text of the license is available at:
\url{https://www.gnu.org/licenses/}.
The git repository of this source code is also available at:
\url{https://github.com/LLyaudet/python-repeatable-iterable/}.


\subsection{
  build\_and\_checks.sh
}
\label{
  build_and_checkssh
}

\VerbatimInput[numbers=left,xleftmargin=-5mm]{
  build_and_checks.sh
}


\subsection{
  CONTRIBUTORS.md
}
\label{
  CONTRIBUTORSmd
}

\VerbatimInput[numbers=left,xleftmargin=-5mm]{
  CONTRIBUTORS.md
}


\subsection{
  .gitignore
}
\label{
  gitignore
}

\VerbatimInput[numbers=left,xleftmargin=-5mm]{
  .gitignore
}


\subsection{
  latex/python-repeatable-iterable.tex.tpl
}
\label{
  latex:python-repeatable-iterabletextpl
}

\VerbatimInput[numbers=left,xleftmargin=-5mm]{
  latex/python-repeatable-iterable.tex.tpl
}


\subsection{
  pyproject.toml
}
\label{
  pyprojecttoml
}

\VerbatimInput[numbers=left,xleftmargin=-5mm]{
  pyproject.toml
}


\subsection{
  README.md.tpl
}
\label{
  READMEmdtpl
}

\VerbatimInput[numbers=left,xleftmargin=-5mm]{
  README.md.tpl
}


\subsection{
  src/python\_repeatable\_iterable/\_\_init\_\_.py
}
\label{
  src:python_repeatable_iterable:__init__py
}

\VerbatimInput[numbers=left,xleftmargin=-5mm]{
  src/python_repeatable_iterable/__init__.py
}


\subsection{
  src/python\_repeatable\_iterable/py.typed
}
\label{
  src:python_repeatable_iterable:pytyped
}

\VerbatimInput[numbers=left,xleftmargin=-5mm]{
  src/python_repeatable_iterable/py.typed
}


\subsection{
  typing\_test/\_\_init\_\_.py
}
\label{
  typing_test:__init__py
}

\VerbatimInput[numbers=left,xleftmargin=-5mm]{
  typing_test/__init__.py
}


\subsection{
  wget\_sha512.sh
}
\label{
  wget_sha512sh
}

\VerbatimInput[numbers=left,xleftmargin=-5mm]{
  wget_sha512.sh
}


Merci Dieu ! Merci P\`ere ! Merci Seigneur ! Merci Saint Esprit !

\end{document}
