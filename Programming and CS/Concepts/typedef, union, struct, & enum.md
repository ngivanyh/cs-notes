---
title: typedef, union, struct, & enum
date created: Thursday, October 30th 2025, 6:15:40 am
date modified: Friday, October 30th 2026, 10:31:21 pm
---
# `typedef`, `union`, `struct`, & `enum`
## `union`
Instead of being able to have multiple different values under a same `enum`. You can store values of **different types** in one `union`.

```c
union int_float_str {
    int integer_val;
    float floating_point_val;
    char * string_val;
};
```

As you can see, this `union` can at one time store either a value of type `int`, `float`, or `char*` (aka string). Members of `union`s are accessed via the same `.`‘s and `->`’s for `struct`. It's the programmer’s responsibility to keep track of whatever’s in the union at the current moment. 

When initializing a new variable that’s something that’s a part of a `union`, the type of the first thing defined in the `union` will be used as the sole initializing type for that variable.

In Python type stubs, you can use the `|` to separate different types, e.g. `int|float`. Or for compatibility, use the `Union[]` from the `typing` library like this: `Union[int, float]`.

## `struct`
A `struct` is a data type that can be specified to have a number of fields, which can have a different type each. 

```c
struct LinkedList {
    int val;
    struct LinkedList * next;
};
```

`struct`s can also have bit-fields, which are sometimes just called fields. 

```c
struct struct_w_bit_fields {
    int one_bit : 1;
    int two_bits : 2;
}
```

Bit-fields can modify the amount of bits a field uses, it's used for alignment (how the "container"(`struct`) is stored in memory), or for simply curbing the amount of memory a field uses. 

In C++, `struct`s also have the ability to contain functions

## `enum`

## `typedef`

#programming #memory #C #cpp 