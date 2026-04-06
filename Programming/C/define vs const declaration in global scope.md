---
tags: [C]
title: define vs const declaration in global scope
date created: Monday, May 5th 2025, 9:58:43 pm
date modified: Monday, April 6th 2026, 8:28:46 am
parent: C
grand_parent: Programming
nav_order: 11
---
# define vs const declaration in global scope
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

In this version, `name` is a variable, and takes up memory, has a type, and could be manipulatable (by removing the `const`). The [[extern]] could be omitted in this situation (same file), but it is still *advisable* to add it (because if you have multiple files, you'd need the `extern`).

#C 