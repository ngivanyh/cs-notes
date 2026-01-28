Similar to the `char*` and `char**` difference in C. If you have a function that accepts `*args`, the things you inputted`args` will then be packed into a tuple.

```python
def print_args(*args):
	print(args)

print_args(1, 2, 3, "hello", "world", "hello, world")
# output: (1, 2, 3, 'hello', 'world', 'hello, world')
```

And `**kwargs` are like the C `**argv`, it'd be easier to show you:

```python
def print_kwargs(**kwargs):
	print(kwargs)

print_kwargs(a="a", one=1, b="b", two=2)
# output: {'a': 'a', 'one': 1, 'b': 'b', 'two': 2}
```

#python #python/features #explanation 