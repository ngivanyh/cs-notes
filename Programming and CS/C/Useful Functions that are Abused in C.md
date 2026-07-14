---
title: Useful Functions that are Abused in C
date created: Wednesday, October 22nd 2025, 4:19:01 pm
date modified: Monday, July 13th 2026, 2:39:06 pm
---
# Useful Functions that are Abused in C
*The names for the input arguments are purely arbitrary*

## `<string.h>`
| Function Name | Input Args                              | Description                                                  |
| ------------- | --------------------------------------- | ------------------------------------------------------------ |
| `strstr`      | `char* s, char* t`                      | Returns index of first occurence of string `t` in string `s` |
| `strcmp`      | `char* s, char* t`                      | Compares string `s` and string `t`                           |
| `strcpy`      | `char* s, char* t`                      | Copies `t` to `s`                                            |
| `memcpy`      | `void* dest, const void* src, size_t n` | Copies `n` bytes from `src` to `dest`                        |

## `<stdlib.h>`
| Function Name | Input Args | Description                                 |
| ------------- | ---------- | ------------------------------------------- |
| `malloc`      | omitted    | omitted—see [[The Two Alllocs in stdlib.h]] |
| `calloc`      | omitted    | omitted—see [[The Two Alllocs in stdlib.h]] |

#C #C/features 