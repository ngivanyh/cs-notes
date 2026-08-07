---
title: The *
date created: Sunday, June 29th 2025, 9:37:25 am
date modified: Saturday, August 1st 2026, 10:19:38 am
---
# The \*
## Arithmetic
...`*` is multiply and `**` to raise to a power.

## `*args` and `**kwargs`
Similar to the `char*` and `char**` difference in C. If you have a function that accepts `*args`, the things you inputted`args` will then be packed into a tuple.

```python
def print_args(*args):
    print(args)

print_args(1, 2, 3, "hello", "world", "hello, world")
# output: (1, 2, 3, 'hello', 'world', 'hello, world')
```

And `**kwargs` are like the C `**argv`, you can provide a key to the argument you pass (hence the shortened name `**kwargs` meaning **K**ey **W**ord **Arg**ument**s**)

```python
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a="a", one=1, b="b", two=2)
# output: {'a': 'a', 'one': 1, 'b': 'b', 'two': 2}
```

Note that `*args` and `**kwargs` are just naming conventions, you can still name them to anything as long as it's in the rules of naming within Python.

## The `*`/`**` Unpack Operators
### `*` Unpack
Presented in [PEP 3132](https://peps.python.org/pep-3132/)

This unpacking operator gets things out of a iterable (not `dict` though), so `list`s, `str`ings, `tuple`s, `set`s. Now for some common uses:

1. Getting the first and rest of a list (and even last): 

```python
first, *rest = seq # valid if len(seq) >= 2
first, *rest, last = seq # same, valid if len(seq) >= 2
```

2. Making `range(n)` a list/tuple:

```python
*a, = range(5) # the comma is there for reasons explained later
```

These *starred expressions* can only be used on the left side of `=` assignments (except for unpacking stuff and inputting them into functions)

#python #python/features  