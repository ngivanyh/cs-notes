---
tags: [C, snippet, C/features]
title: const int*, float*, and others (excluding void* and char*)
date created: Tuesday, July 1st 2025, 4:06:33 pm
date modified: Sunday, April 5th 2026, 10:21:14 pm
parent: C
grand_parent: Snippets
nav_order: 7
---
# const int\*, float\*, and others (excluding void\* and char\*)
```c
const int* a = (const int[])[1,2,3];
```

The `const` applies the `const` to ALL the values in the array, same goes for types like `long`, `float`, and `double`.

#C #snippet #C/features 