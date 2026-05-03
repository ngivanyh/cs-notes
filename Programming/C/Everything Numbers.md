---
title: Everything Numbers
date created: Friday, April 3rd 2026, 10:59:15 pm
date modified: Sunday, May 3rd 2026, 10:28:10 pm
tags: [C, memory]
parent: C
nav_order: 3
---
# Everything Numbers
## Types of Numbers
- **The Standard Roster**
    - `int`
    - `long`
    - `long long`
    - `usigned (number type)`
    - `float`
    - `double`
    - `long double`
- **Extra Guys from `stdint.h`**
    - `uint(2/8/16/32/64)_t`
    - `int(2/8/16/32/64)_t`

## Annoyances of Floating Point Numbers
### Precision
### Epsilon ($\epsilon$)
Since there is an underlying precision issue in floating point numbers, people set a $\epsilon$ as a boundary of sorts. If $x<\epsilon$ then $x$ is essentially "0"

## Arithmetic
### Those in `math.h`
| Function    | Description                 |
| ----------- | --------------------------- |
| `pow(x, y)` | $x^y$, **returns `double`** |
| `sin(x)`    | $\sin x$                    |
| `cos(x)`    | $\cos x$                    |
| `tan(x)`    | $\tan x$                    |
| `sqrt(x)`   | $\sqrt{n},n>=0$             |
| `fabs(x)`   | $\|x\|$                     |
| `exp(x)`    | $e^x$                       |
| `log(x)`    | $\log_e x$                  |
| `log10(x)`  | $\log_{10} x$               |
| `log2(x)`   | $\log_2 x$                  |

### Those in `stdlib.h`
| Function | Description                 |
| -------- | --------------------------- |
| `rand()` | $x^y$, **returns `double`** |
| `sin(x)` | $\sin x$                    |
|          |                             |

`frand()` for a random number between 0 and 1
`srand()` (unsigned) seed for `rand()`

#C #memory 