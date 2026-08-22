---
title: Set
date created: Thursday, November 20th 2025, 10:14:11 pm
date modified: Tuesday, August 11th 2026, 3:01:50 pm
---
# Set
## Python
They are:
- Unordered
- Can store a mixture of types (like `tuple`)
- Cannot have duplicates
- Don't have indices (so no `SET[i]`), and no slicing
- Immutable **elements** (once you have an item in a `set`, it cannot be changed)
- Uses hashing internally (e.g. Membership checking is $O(1)$)

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
See the [[Deleting#Set Element Deletion|"Set Element Deletion" section in "deleting stuff"]].

### `frozenset`
The truly immutable `set`. 

## C++

#data-structures  #python #python/features 