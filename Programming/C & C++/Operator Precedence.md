---
tags: [C, C/conceptual]
title: Operator Precedence
date created: Wednesday, October 29th 2025, 3:32:40 pm
date modified: Wednesday, May 6th 2026, 2:17:20 pm
parent: C & C++
nav_order: 6
---
# Operator Precedence
## Operator Precedence Table
C has a a lot of implied behavior, operator chaining, and undefined behavior traps. Hence the importance of operator precedence. 

*Empty cells copy the same contents as the one above it.*

| Precedence | Operator            | Description                                                 | Associativity |
| ---------- | ------------------- | ----------------------------------------------------------- | ------------- |
| 1          | `()`                | Parentheses (function call)                                 | Left-to-Right |
|            | `[]`                | Array access                                                |               |
|            | `.`                 | For `structs` (access fields)                               |               |
|            | `->`                | `struct` `.` and dereference (`*`)                          |               |
|            | `++`, `--`          | Postfix increment and decrement                             |               |
| 2          | `++`, `--`          | Prefix increment, decrement                                 | Right-to-Left |
|            | `+`, `-`            | Unary plus/minus, related to the signs of numbers (pos/neg) |               |
|            | `!`, `~`            | Logical NOT, Bitwise complement                             |               |
|            | `(type)`            | Type casting                                                |               |
|            | `*`                 | Dereference operator                                        |               |
|            | `&`                 | Get memory address                                          |               |
|            | `sizeof`            | Get the size of something in bytes                          |               |
| 3          | `*`, `/`, `%`       | Multiplication, division, modulus                           | Left-to-Right |
| 4          | `+`, `-`            | Addition, subtraction                                       | Left-to-Right |
| 5          | `<<`, `>>`          | Bitwise shift left, Bitwise shift right                     | Left-to-Right |
| 6          | `<`, `<=`           | Less than, less than or equal to                            | Left-to-Right |
|            | `>`, `>=`           | Greater than, greater than or equal to                      |               |
| 7          | `==`, `!=`          | Is equal to, is not equal to                                | Left-to-Right |
| 8          | `&`                 | Bitwise AND                                                 | Left-to-Right |
| 9          | `^`                 | Bitwise XOR                                                 | Left-to-Right |
| 10         | `\|`                | Bitwise OR                                                  | Left-to-Right |
| 11         | `&&`                | Logical AND                                                 | Left-to-Right |
| 12         | `\|\|`              | Logical OR                                                  | Left-to-Right |
| 13         | `? (expr) : (expr)` | `(CONDITION) ? (expr) : (expr)` (Tenary conditional)        | Right-to-Left |
| 14         | `=`                 | Assignment                                                  | Right-to-Left |
|            | `+=`, `-=`          | Addition, subtraction assignment                            |               |
|            | `*=`, `/=`          | Multiplication, division assignment                         |               |
|            | `%=`, `&=`          | Modulus, bitwise AND assignment                             |               |
|            | `^=`, `\|=`         | Bitwise exclusive, inclusive OR assignment                  |               |
|            | `<<=`, `>>=`        | Bitwise shift left, right assignment                        |               |
| 15         | `,`                 | Comma (expression separator)                                | Left-to-Right |

## Postfix vs Prefix

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

It doesn't really matter, purely user preference.

What about expressions like these?

```c
int a[3] = {1, 2, 3};
int i = 3;

while (i--)
{
    ... // code
}
```

```c
int a[3] = {1, 2, 3};

int * b = a;
for (int i = 0; i < 3; ++i)
    *b++ = 0; // set everything to 0
```

Remember that postfix `++` or `--` doesn't increment on the spot, AND it first returns the current value of the variable (the value before it pluses/minuses 1). It will increment once the expression is finished. It's like a "I will increment soon" signal. 

So the `i--` on the first iteration will go through because the `while` loop condition is `while (3)`, but once you go into the loop body, `i` is 2.

#C #C/conceptual 