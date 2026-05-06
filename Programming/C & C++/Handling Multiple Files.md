---
tags: [C, C/conceptual]
title: Handling Multiple Files
date created: Wednesday, September 10th 2025, 7:10:43 pm
date modified: Wednesday, May 6th 2026, 2:16:33 pm
parent: C & C++
nav_order: 5
---
# Handling Multiple Files
## `extern` variables and functions:
- Not strictly necessary
- The *initialization* happens in the source file, so in the other programs you're *declaring* it as an external variable, it doesn't reserve any extra space to accommodate. 
- If you have an `extern` array. They size need not to be declared. (E.g. *file1*: `int arr[SIZE]`, *file2*: `extern int arr[]`)
- Only one *definition* is allowed of that external variable/function.
- TL;DR -> You can **declare** external variables with `extern`, and it can help discern the internal variables, from the external.

## Compilation of Multi-file Programs:

`cc`:

```
$ cc abc.c def.c ghi.c
```

## Single Header Libraries
One `.h` file to contain a whole C library

```c
#ifndef INCLUDE_GUARD
#define INCLUDE_GUARD // prevent repeated includes, causing errors

#ifdef __cplusplus
extern "C" {
#endif // __cplusplus

#ifdef __cplusplus
}
#endif // __cplusplus

#endif // INCLUDE_GUARD

// library implementation
#ifdef LIBRARY_IMPLEMENTATION
#endif
```

#C  #C/conceptual 
