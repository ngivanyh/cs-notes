---
tags: [C, C/conceptual, memory, programming]
title: Pointers
date created: Wednesday, September 17th 2025, 3:31:03 pm
date modified: Saturday, July 11th 2026, 9:45:44 pm
parent: C & C++
nav_order: 5
---
# Pointers
## "Regular" Pointers (Variable Pointers)
Pointers can do arithmetic, but if you have `int a[3] = {1, 2, 3}`, then when you access the second element with `a[1]`, C will automatically convert that into `*(a + 1)`. You might think that `+1` is just plus one like in maths, but in reality, since an `int` is four bytes, it really means "jump" by `1 * sizeof(int)` bytes.

### Stupid What Ifs:
- If `p` points to `0x10` and `q` points to `0x11`, `q - p < NULL` *might* result in `true`, but what we know is that the value would be useless as it'd point to a garbage location, and because pointers are unsigned, *maybe* it will overflow back and become `0xMAX - 0x-1`. (And it's also very stupid.
- Because in normal circumstances, `-1` on `type` pointer doesn't actually deduct one, if you were delusional, it wouldn't be easy to treat an (say) `int*` as a normal number.
- Trying to bypass the `const` limitation via code like the below is **undefined behavior**, i.e. anything can happen:

```c
#include <stdio.h>

int main(void)
{
    const int a = 1;
    int * b = (int *) & a;
    *b = 5;
    printf("a: %d, b: %d\n", a, *b);
    return 0;
}
```

### `void *`
C's version of "generics" (variables of a generic type, aka, no specific type), but for pointers (the non-pointer equivalent doesn't exist).

E.g. the `free()` function is a function that accepts the pointer to the memory you want to free as `void*`, since it frees anything of any type. 

### Easier Pointer Reading
#### Setting the Better Naming Scheme
The most confusion-free way to declare pointers is to separate spaces for every element in the declaration, including the `*`. Examples:

- `const * double a`
- `unsigned long long * const b`
- `int * c`
- `static double * a`

#### Reading from Right to Left
Now that we've separated these things, reading them from right to left makes everything clear as day. Before, things like `const double * a` and `double * const a` seem very much like the same, but reading from right to left will differentiate them:

`const double * a` is a pointer `a` that points to a `const double`
`double * const a` is a `const` pointer `a` that points to a `double`

## Difference between Pointers and Arrays
Arrays and pointer have a lot in common. They are basically one with the other in C. But there are differences.

An ==**array**== is a contiguous chunk of values stored in memory. While a ==**pointer**== is a address to a specific place in memory. 

So, the saying of not being able to get the size of a array in C is not totally wrong. But in the example here you can actually get the array size:

```c
int arr[3];
printf("%lu", sizeof(arr)); // prints 12, meaning 12 bytes
```

So, you still can't get the array size from pointers, because they can point to anything; random addresses, array elements, `NULL`, single integers, etc. 

But when you pass an array into a function, you are automatically passing the **pointer** to the first element of the array. So, a lot of times, arrays will *decay* into pointers. 

## Function Pointers
Pointers to functions can be assigned, placed in arrays, passed into functions, returned by functions and so on. (basically like a normal pointer)

Format: `RETURN_TYPE (*NAME)(INPUT_ARGS)`

The `()` are needed for `NAME` as without it, it now means a function who'll return a pointer pointing to a value of `RETURN_TYPE`.

### Its Bewildering Notations
Some examples of function pointers: 
- `int (*f)()`: A pointer to a function returning `int`
- `char (*(*x())[])()`: `x` is a function returning pointer to `array[]` (`(*x())[]`) of pointer to function returning `char` (`char . . .(*x())[])()`)
- `char (*(*x[3])())[5]`: `x` is an `array[3]` of pointer (`(*x[3])`) of a function returning pointer to `array[5]` of `char`.

This thing is basically like throwing functions around in Python, except with the extra syntax of pointers.

#C  #C/conceptual #memory #programming 