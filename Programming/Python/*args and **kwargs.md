---
tags: [python, python/features]
title: "*args and **kwargs"
date created: Sunday, June 29th 2025, 9:37:25 am
date modified: Monday, April 6th 2026, 8:28:46 am
parent: Python
nav_order: 1
---
# \*args and \*\*kwargs
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

#python #python/features  