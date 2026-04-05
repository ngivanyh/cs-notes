---
tags: [C, C/features]
title: printf and scanf notation
date created: Wednesday, November 19th 2025, 2:32:41 pm
date modified: Sunday, April 5th 2026, 10:21:14 pm
parent: C
grand_parent: Snippets
nav_order: 9
---
# printf and scanf notation

| Character | Printed As                                                                           |
| --------- | ------------------------------------------------------------------------------------ |
| `d`, `i`  | Integer, `int`                                                                       |
| `li`      | `long`                                                                               |
| `o`       | Unsigned octal number (without leading zero, e.g. `0o`)                              |
| `x`, `X`  | Unsigned hexadecimal number (without `0x` or `0X`), `abcdef` or `ABCDEF` for 10 – 15 |
| `u`       | Unsiged decimal number                                                               |
| `c`       | Single character, `char`                                                             |
| `s`       | `char*`                                                                              |
| `f`       | `float` (`m.nnnnnnnnnn`, precision decided before the `f`)                           |
| `lf`      | `double` (`m.nnnnnnnnnn`, precision decided before the `lf`)                         |
| `e`, `E`  | `float` and `double` (`m.nnnnnnn e^x`/`m.nnnnnnn E^x`)                               |
| `p`       | `void*`, implementation dependent                                                    |

So you type the `%`, in between the character (`s`, `i`, `d`, etc), you can put in these things (in order).

- A minus sign, indicating left adjustment (padding/min field width)
- A number for the minimum field width, will be padded on the left if there's no `-` (in front, and also when the thing you're printing is less than the min field width)
- Period for precision
- Number of chars to print, or the number of digits after the floating point, or the min digits for an integer

It's almost the same for `scanf()` (but no `p` amongst others), it's just the removal of the capitals (`X`, `E`, etc). Also between the `%` and the character, there could be a `*` assignment suppression character.

> [!NOTE] 
> `scanf()` also returns the number of elements read from `stdin`.

`sscanf` is a function that reads from a string (`char *`), instead of `stdin`.

#C #C/features 