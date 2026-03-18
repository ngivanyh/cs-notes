---
tags: [python, python/features]
title: sets
date created: Thursday, November 20th 2025, 10:14:11 pm
date modified: Wednesday, March 18th 2026, 2:41:37 pm
---
# sets
## `set`
They are:
- Unordered
- Can store a mixture of types (like `tuple`)
- Cannot have duplicates
- Don't have indices (so no `SET[i]`), and no slicing
- Immutable **elements** (once you have an item in a `set`, it cannot be changed)
- Uses hashing internally (so more efficient than `list` sometimes)

> [!NOTE]
>  `True` and `1` are the same thing in sets, so are `False` and `0`, the reason should be pretty obvious.

You declare a set like this:

```python
a = {1, 2, 3}
b = set(DATA) # DATA can be either a list or a tuple

c = set() # empty set
```

> [!WARNING]
> Empty sets must be declared using the `set()` function instead of empty square brackets as those are reserved for generating an empty `dict`.

### Create 

```python
a = {1, 2, 3}
a.add(4)
```

### Read

```python
a = {1, 2, 3}

for element in a:
    ...
```

```python
a = {1, 2, 3}
iter_a = iter(a)
e = next(iter_a)
```

The only ways are basically using iterators

### Delete
See the [[deleting stuff#Set Element Deletion|"Set Element Deletion" section in "deleting stuff"]].

## `frozenset`
The truly immutable `set`. 

#python #python/features 