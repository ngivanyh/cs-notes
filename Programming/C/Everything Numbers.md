---
title: Everything Numbers
date created: Friday, April 3rd 2026, 10:59:15 pm
date modified: Thursday, April 9th 2026, 6:50:47 pm
tags: [C]
parent: C
nav_order: 3
---
# Everything Numbers
## Types of Numbers
- **The Standard Roster**
    - `int`
    - `long`
    - `long long`
    - `usigned (number)`
    - `float`
    - `double`
    - `long double`
- **Extra Guys from `stdint.h`**
    - `uint(2/8/16/32/64)_t`
    - `int(2/8/16/32/64)_t

## maths
`#include <math.h>` first

| Function    | Description                 |
| ----------- | --------------------------- |
| `pow(x, y)` | $x^y$, **returns `double`** |
| `sin(x)`    | $\sin x$                    |
| `cos(x)`    | $\cos x$                    |
| `atan2(x)`  | arctangent                  |
| `sqrt(x)`   | $\sqrt{n},n>=0$             |
| `fabs(x)`   | $\|x\|$                     |
| `exp(x)`    | $e^x$                       |
| `log(x)`    | $\log_e x$                  |
| `log10(x)`  | $\log_{10} x$               |
| `log2(x)`   | $\log_2 x$                  |

`frand()` for a random number between 0 and 1
`srand()` (unsigned) seed for `rand()`

#C 