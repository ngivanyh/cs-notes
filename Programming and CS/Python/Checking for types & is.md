---
title: Checking for types & is
date created: Saturday, September 6th 2025, 2:57:23 pm
date modified: Wednesday, May 6th 2026, 2:45:09 pm
---
# Checking for types & `is`
## Check for Types
Check if variable is an instance of a type (e.g. `str`, `int`, `bool`)

```python
if isinstance(var, type):
```

Check if the value is JUST that type

```python
if type(var) is type:
```

## `is`
`is` checks for their *"true nature"* (types), and can only be used to compare between those two things. 

```python
1 is int # False

a = None
a is None # True

b = True
b is True # True
b is False # False
```


#python #snippet #python/features 