# Useful-dev

The following items represents useful knowledge on a developer daily basis. Things that help you, at least, to understand how tools work and make your job easier [(source)](https://twitter.com/TheEduardoRFS/status/1407702694467407873).

1. Recursion
2. Trees and basic operations on them
3. Write a bad parser
4. Interpret the lambda calculus

## Recursion
Recursion is the same as loops. Literally any loop can be written with recursion and vice-versa. That's why trees are mentioned in second place above. Trees without recursion is terrible.

## Trees and basic operations on them
There are quite a lot of data structures over there. Take a look at graphs for example, it's an insane field. Trees are a subset of graphs which is used it in practice. Because code is a tree as also like data derived from code (such as JSON).

## Write a bad parser
The best way to understand motivations of an [Abstract Syntax Tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) is writing a parser for it. Besides, it helps to debug code. When you get an error at line 182 in a file with 181 lines you know its happening because something wasn't closed, so the parser is waiting for a token that doesn't exist.

## Interpret the lambda calculus
The lambda calculus is a formal system based on functions and operators where they can be combined to form another operators. It's the mathematical basis for what it is most modern in programming languages.

## Run examples
On the command line, type the following:
```
python folder/file.py
```
