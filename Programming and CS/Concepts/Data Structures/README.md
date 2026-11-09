---
date created: Saturday, July 11th 2026, 5:27:10 pm
date modified: Saturday, November 7th 2026, 9:09:35 am
title: README
---
# README
This directory will write about data structures of all kinds, including how to write and use them in C, C++, and Python. The programming language used will have their respective tags in the markdown file.

> [!NOTE]
> These notes do not document all the possible functionality from the libraries that implement these data structures and operations on them

## `collections`, `queue`, `heapq`, and `bisect`
This is where the bulk of Python's extended data structures are put in. `collections` is a collection of types, while `queue`, `heapq`, and `bisect` are more specialized around a data type. Not quite comparable to C++'s [STLs](#stls) though, especially in performance.

## STLs
The **S**tandard **T**emplate **L**ibrary, also shortened as **STL(s)**, are a set of data types implemented using C++ templates that provide beyond the rudimentary data types and structures found in C. When you are painstakingly typing out your `typedef`s and thinking of how to implement it, C++ may already have a standardized library of such things.

**Before**:

```c
// singly linked list storing integers
typedef struct int_linked_list {
    int value;
    struct int_linked_list * next;
} int_linked_list;
```

**After**:

```cpp
#include <vector>

vector<int> resizable_int_list;
```

~~`typedef struct`~~ → STLs (`vector`, `queue`, `pair`, etc)

STLs, evidently, uses C++ templates, but basically you put the type you want into the `<>`'s. So, it can be simple things like `int`, `float`, or `bool`; but it can also be things like other STLs, like: `pair`, `vector`, and more!

#readme #data-structures #cpp #cpp/features #python #python/features 