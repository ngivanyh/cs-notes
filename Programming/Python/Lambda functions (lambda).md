A Python `lambda` function is a small function that can take any number of arguments, but the return must **only** be in one expression. `lambda` functions are unnamed. 

Essentially, functions like this:

```python
def func(*args):
    return [expression]
```

To this:

```
lambda [args]: [expression]
```

Some way to think of the uses of these are functions that are short, and really one liners. Then a `lambda` function would be a good use case of it.

#python #python/features  