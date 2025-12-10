```python
__add__
__sub__
__mul__
__truediv__
__pow__
__neg__
__repr__
__rad__
__rsub__
__rmul__
__rtruediv__
```

Say you have a class `c`, and two variable of type `c` (let's call them `a` and `b`) if you do the following, it won't really have any desired result.

```python
class c:
	def __init__(self):
		...
	...

a = c()
b = c()
```

```python
a + b
a * b
a ** b
a / b
-a
a + 2
6 * b
print(a)
```