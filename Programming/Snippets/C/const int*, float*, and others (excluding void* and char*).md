---
tags: [C, snippet, C/features]
title: const int*, float*, and others (excluding void* and char*)
date created: Tuesday, July 1st 2025, 4:06:33 pm
date modified: Saturday, February 28th 2026, 12:27:24 pm
---
```c
const int* a = (const int[])[1,2,3];
```

The `const` applies the `const` to ALL the values in the array, same goes for types like `long`, `float`, and `double`.

#C #snippet #C/features 