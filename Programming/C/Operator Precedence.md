---
tags: [C, C/conceptual]
title: Operator Precedence
date created: Wednesday, October 29th 2025, 3:32:40 pm
date modified: Saturday, February 28th 2026, 9:31:03 pm
---
# Operator Precedence
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

#C #C/conceptual 