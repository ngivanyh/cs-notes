---
title: Immutability vs Constants and the Other Keywords for Variables in C
date created: Tuesday, July 7th 2026, 2:24:47 pm
date modified: Wednesday, July 8th 2026, 8:19:34 pm
---
# Constants Compared and the Other Keywords for Variables in C

## Immutability vs Constants
**Immutability**: Unchangeable variable, can be dynamically created and used.
**Constant**: *Also* an unchangeable variable, **==must be defined at compile time==** (i.e. the compiler needs to know what it is)

## `define` vs Constants

```c
#define NAME VAL
```

When compiled, the compiler will simply just *replace* all instances of `NAME` throughout the program. It has no type, and does not take up any memory (RAM). (preprocessor)

```c
const type name = val;

int main(void)
{
    ... /* some code executed */
    
    /* and you can access the variable with */
    extern name ... /* some action to the external value */
}
```

In this version, `name` is a variable, and takes up memory, has a type, and could be manipulatable (by removing the `const`). The [[Dealing with Compilation#`extern` variables and functions|extern]] could be omitted in this situation (same file), but it is still *advisable* to add it (because if you have multiple files, you'd need the `extern`).

## Other Variable Keywords (in C)
Besides `int`, `float`, `double`, `char`, `unsigned`, `signed`, and the other basic stuff.

### `static`
`static` variables exist in the data portion of a program. They are only initialized once, and they can persist throughout the execution of the program. They are also ***strictly*** internal, and they only exist in the scope they were defined in. For example:

```c
#include <stdio.h>

void add_numbers()
{
    static a = 10;
    int b = 10;
    
    a += 5;
    b += 5;
    
    printf("a: %d, b: %d", a, b); 
}

int main(void)
{
    add_numbers();
    add_numbers();
    add_numbers();
    
    return 0;
}
```

The output will be:

```c
a: 15, b: 15
a: 20, b: 15
a: 25, b: 15
```

So they are useful for fixes circumventing the fact that you can't return pointers. But they aren't thread-safe (safe from other threads of execution, if your program is multithreaded), so just use `malloc()`.

#programming #C #C/features 