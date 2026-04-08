---
tags: [python, python/features]
title: Special Class Methods (besides from __init__)
date created: Wednesday, December 10th 2025, 10:24:44 pm
date modified: Monday, April 6th 2026, 8:28:47 am
parent: Python
nav_order: 11
---
# Special Class Methods (besides from \_\_init\_\_)
```python
__add__
__sub__
__mul__
__truediv__
__pow__
__neg__
__repr__
__radd__
__rsub__
__rmul__
__rtruediv__
__call__
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
a + b # error!
a - b # error!
a * b # error!
a / b # error!
a ** b # error!
-a # error!
a + 2 # error!
6 * b # error!
print(a) # doesn't really print anything useful
```

These special class methods tell Python what to do when you do the operations above. 

[The full list of special class methods](https://docs.python.org/3/reference/datamodel.html#specialnames)

More about OOP: [[OOP Things]]

#python #python/features 