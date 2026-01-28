It's kinda like a operator for checking types, but only for types, so `1 is int` cannot work. It can only work between **types**. Useful for checking things like `val is None`, `val is True`, `val is False`.

Another way to understand it is that `is` checks for their *"true nature"* (types), and can only be used to compare between those two things. 

```python
1 is int -> False

a = None
a is None -> True

b = True
b is True -> True
b is False -> False
```

#python #python/features #explanation 