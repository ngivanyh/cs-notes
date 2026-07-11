---
title: IO in C
date created: Wednesday, July 8th 2026, 10:25:44 am
date modified: Saturday, July 11th 2026, 9:51:05 pm
tags: [C, C/features]
parent: C & C++
nav_order: 4
---
# IO in C
## Formatted Printing and Scanning
### Notation

| Character | Printed/Scanned As                                                                   |
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

- A `-`, indicating left adjustment (padding/min field width)
- A number for the minimum field width, will be padded on the left if there's no `-` (in front, and also when the thing you're printing is less than the min field width)
- `.` for precision
- Number of chars to print, or the number of digits after the floating point, or the min digits for an integer

**Exceptions for scanning:** It's almost the same, it's just the removal of the capitals (`X`, `E`, etc) and `p`. Also between the `%` and the character, there could be a `*` assignment suppression character.

### Functions
 - **Files**
     - `fprintf(FILE * f, char * format_str, ...);`
     - `fscanf(`
 - **`stdin`**
     - `printf(char * format_str, ...);`
     - `scanf(char * format_str, ...);`

## Files

#C #C/features 