---
tags: [C, C/features, C/conceptual]
title: Function Pointers (and confusing notations)
date created: Wednesday, October 22nd 2025, 4:19:01 pm
date modified: Saturday, February 28th 2026, 9:31:03 pm
---
# Function Pointers (and confusing notations)
Pointers to functions can be assigned, placed in arrays, passed into functions, returned by functions and so on. (basically like a normal pointer)

Format: `RETURN_TYPE (*NAME)(INPUT_ARGS)`

The `()` are needed for `NAME` as without it, it now means a function who'll return a pointer pointing to a value of `RETURN_TYPE`.

Some examples of function pointers: 
- `int (*f)()`: A pointer to a function returning `int`
- `char (*(*x())[])()`: `x` is a function returning pointer to `array[]` (`(*x())[]`) of pointer to function returning `char` (`char (*x . . . ])()`)
- `char (*(*x[3])())[5]`: `x` is an `array[3]` of pointer (`(*x[3])`) of a function returning pointer to `array[5]` of `char`.

This thing is basically like throwing functions around in python, except with the extra syntax of pointers.

#C #C/features  #C/conceptual 