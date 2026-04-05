---
tags: [C, snippet]
title: Swapping Two Ints (Not recommended) Without a Temporary Variable with Bitwise XOR
date created: Friday, May 30th 2025, 10:32:17 am
date modified: Sunday, April 5th 2026, 10:21:14 pm
parent: C
grand_parent: Snippets
nav_order: 5
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