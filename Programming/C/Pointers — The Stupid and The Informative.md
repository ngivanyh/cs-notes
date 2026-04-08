---
tags: [C, C/conceptual, memory]
title: Pointers — The Stupid and The Informative
date created: Wednesday, September 17th 2025, 3:31:03 pm
date modified: Monday, April 6th 2026, 8:28:46 am
parent: C
nav_order: 10
---
# Pointers — The Stupid and The Informative
Pointers can do arithmetic, but if you have `int a[3] = {1, 2, 3}`, then when you access the second element with `a[1]`, C will automatically convert that into `*(a + 1)`. You might think that `+1` is just plus one like in maths, but in reality, since an `int` is four bytes, it really means "jump" by `1 * sizeof(int)` bytes.

## Stupid What Ifs:
- If `p` points to `0x10` and `q` points to `0x11`, `q - p < NULL` *might* result in `true`, but what we know is that the value would be useless as it'd point to a garbage location, and because pointers are unsigned, *maybe* it will overflow back and become `0xMAX - 0x-1`. (And it's also very stupid.
- Because in normal circumstances, `-1` on `type` pointer doesn't actually deduct one, if you were delusional, it wouldn't be easy to treat an (say) `int*` as a normal number.
- Trying to bypass the `const` limitation via code like the below is **undefined behavior**, i.e. anything can happen:

    ```c
    #include <stdio.h>

    int main(void)
    {
        const int a = 1;
        int* b = (int*) &a;
        *b = 5;
        printf("a: %d, b: %d\n", a, *b);
        return 0;
    }
    ```

## `void*`
C's version of "generics" (variables of a generic type, aka, no specific type), but for pointers (the non-pointer equivalent doesn't exist).

E.g. the `free()` function is a function that accepts the pointer to the memory you want to free as `void*`, since it frees anything of any type. 

#C  #C/conceptual #memory 