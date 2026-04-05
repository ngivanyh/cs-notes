---
tags: [programming]
title: for Loops (C Style)
date created: Friday, June 27th 2025, 9:55:58 am
date modified: Sunday, April 5th 2026, 10:21:14 pm
parent: General Programming and Comp Sci
grand_parent: Programming
nav_order: 15
---
# for Loops (C Style)
```c
for (int i = 0; i < val; ++i)
{
    // loop body goes here
}
```

After the first iteration, `++i` gets executed, then `i < val` gets evaluated, if `i < val` is `false` then we exit the loop, if it's true, the loop re-executes.

On the initialization (`int i = 0`), the condition gets evaluated (`i < val`), then the loop body gets ran.

`for` loops can also be used to juggle multiple values at once, separate expressions using the `,` operator.

#programming 