---
title: Deleting
date created: Wednesday, July 2nd 2025, 4:46:47 pm
date modified: Friday, August 7th 2026, 10:56:16 am
---
# Deleting
## `del`
`del`etes objects, since about everything in Python is a object, `str`, `int`, `float`, `list`s, etc. It is basically the incinerator in Python. But it doesn't **deallocate** memory, it ***==removes a reference==*** to the thing you're deleting, it only frees stuff because you've removed every last reference of that thing your deleting, then the garbage collector will pretty soon realize it can free that memory, therefore the memory is freed. 

## List Element Deletion
### `del`

```python
a = [1,2,3]

del a # the whole thing
del a[i] # the thing at index i
del a[start:end] # deletes everything in that slice
```

### `list.remove(value)`

```python
a = [1,2,3]

a.remove(1)
print(a) # [2,3]
```

### `list.pop(index)`

Without the index, this will pop the last item, essentially making it a stack by using it with `.append()`.

```python
a = [1,2,3]

print(a.pop(2)) # prints the value of the thing removed, in this case: 3
print(a) # [1,2]
```

> [!NOTE]
> This can be slow, especially the further in front you're deleting, as Python has to move the elements from the back to the front

## Dictionary Element Deletion
### `del`

```python
a = {
    1: 2,
    3: {4: 5},
    4: {
	    5: {6: 7}
    }
}

del a # the whole thing
del a[1] # the {1: 2} key value pair
del a[4][5] # the {5: {6, 7}} key value pair
```

### `dict.pop(key)`

```python
a = {
    1: 2,
    3: {4: 5},
    4: {
	    5: {6: 7}
    }
}

new_a = a.pop(1) # the {1: 2} key value pair
```

## Set Element Deletion

#python #python/features  