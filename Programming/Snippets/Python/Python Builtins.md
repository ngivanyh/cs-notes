---
tags: [python, python/features]
title: Python Builtins
date created: Saturday, January 31st 2026, 9:37:58 am
date modified: Friday, March 6th 2026, 9:22:54 pm
---
# Python Builtins

| Builtin Name              | Type (class method, iterator, function, etc) | Description                                                                                                                | Example                                    |
| ------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| `enumerate()`             | Iterator                                     | Returns a tuple of the index and value of a iterator                                                                       | `for i, val in enumerate(list): ...`       |
| `reversed()`              | Iterator                                     | Iterates over a iterator in reverse direction                                                                              | `for val in reversed(list): ...`           |
| `zip()`                   |                                              |                                                                                                                            |                                            |
| `sorted()`                | Function                                     | Sorts an iterator, there is an `key=` argument which can specify the key for sorting (what it sorts by) (takes a function) | `sorted(iterator)`                         |
| `all()`                   |                                              |                                                                                                                            |                                            |
| `map()`                   | Function                                     | Takes two arguments, the first of which is a function will will be applied on the second argument (should be an iterator)  | `s = ["1", "2", "3"]; int_s = map(int, s)` |
| `bin()`, `hex()`, `oct()` | Function                                     | Turns an `int` into a binary, hexadecimal, or octal string.                                                                |                                            |
|                           |                                              |                                                                                                                            |                                            |

#python #python/features 