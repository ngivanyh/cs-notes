---
title: union & struct
date created: Thursday, October 30th 2025, 6:15:40 am
date modified: Friday, August 7th 2026, 9:42:36 am
---
# `union` & `struct`
## `union`
Instead of being able to have multiple different values under a same `enum`. You can store values of **different types** in one `union`.

```c
union {
    int integer_val;
    float floating_point_val;
    char* string_val;
} eg;
```

As you can see, this `union` can at one time store either a value of type `int`, `float`, or `char*` (aka string). Members of `union`s are accessed via the same `.`‘s and `->`’s for `struct`. It's the programmer’s responsibility to keep track of whatever’s in the union at the current moment. 

When initializing a new variable that’s something that’s a part of a `union`, the type of the first thing defined in the `union` will be used as the sole initializing type for that variable.

In Python type stubs, you can use the `|` to separate different types, e.g. `int|float`. Or for compatibility, use the `Union[]` from the `typing` library like this: `Union[int, float]`.

## `struct`


#programming #memory #C 