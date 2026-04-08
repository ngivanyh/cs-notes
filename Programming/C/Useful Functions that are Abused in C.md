---
tags: [C, C/features]
title: Useful Functions that are Abused in C
date created: Wednesday, October 22nd 2025, 4:19:01 pm
date modified: Monday, April 6th 2026, 8:28:47 am
parent: C
nav_order: 16
---
# Useful Functions that are Abused in C
*The names for the input arguments are purely arbitrary*

## `<string.h>`
| Function Name | Input Args         | Description                                                  |
| ------------- | ------------------ | ------------------------------------------------------------ |
| `strstr`      | `char* s, char* t` | Returns index of first occurence of string `t` in string `s` |
| `strcmp`      | `char* s, char* t` | Compares string `s` and string `t`                           |
| `strcpy`      | `char* s, char* t` | Copies `t` to `s`                                            |
| `memcpy`      |                    |                                                              |
## `<stdlib.h>`
| Function Name | Input Args | Description                                 |
| ------------- | ---------- | ------------------------------------------- |
| `malloc`      | omitted    | omitted—see [[The Two Alllocs in stdlib.h]] |
| `calloc`      | omitted    | omitted—see [[The Two Alllocs in stdlib.h]] |

#C #C/features 