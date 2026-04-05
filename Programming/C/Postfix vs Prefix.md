---
tags: [C, C/conceptual]
title: Postfix vs Prefix
date created: Monday, May 5th 2025, 7:51:40 pm
date modified: Saturday, March 14th 2026, 9:55:12 pm
parent: C
grand_parent: Programming
---
# Postfix vs Prefix

```c
#include <stdio.h>

int main(void)
{
    int i, j = 0;
    printf("i: %d j: %d", i++ + 1, ++j + 1);
    return 0;
}
```

Postfix returns the value of the variable first, then does the increment (or decrement w/ ```i--
``` or ```j--```), and the opposite goes for prefix.

So the value of the printf for ```i++ + 1``` would be 1, but after that, ```i```'s value would be `1` (due to `i++`). And the value for `++j + 1` would be 2, but since the `+ 1` isn't a `+=` ,`++`, or something similar, `j`'s value would be 1 (again, due to `++j`).

When you're declaring a `for` loop: (etc)

```c
for (int i = 0; i < n; ++i)
    ;
```

It doesn't really matter, purely user preference. [[Operator Precedence|However, when you string this up with other operators, that's when the positions matter]].

#C  #C/conceptual 