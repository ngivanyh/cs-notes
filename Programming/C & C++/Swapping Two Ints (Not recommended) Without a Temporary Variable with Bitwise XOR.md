---
tags: [C, snippet]
title: Swapping Two Ints (Not recommended) Without a Temporary Variable with Bitwise XOR
date created: Friday, May 30th 2025, 10:32:17 am
date modified: Saturday, April 11th 2026, 9:53:49 pm
parent: C & C++
nav_order: 11
---
# Swapping Two Ints (Not recommended) Without a Temporary Variable with Bitwise XOR

```c
#include <stdio.h>

int main(void)
{
    int a = 5;
    int b = 4;

    a ^= b;
    b ^= a;
    a ^= b;

    // now a = 4, b = 5

    return 0;
}
```

`a ^= b`: Gets the difference of `a` and `b`
`b ^= a`: Makes up the difference between `b` and `a`, making `b` `a`'s original value
`a ^= b`: Uses that difference to recover `b`'s original value

For more bitwise ops: [[Bitwise Operators]]

#C #snippet  