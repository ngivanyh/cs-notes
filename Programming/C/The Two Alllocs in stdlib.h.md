---
tags: [C, C/features, memory]
title: The Two Alllocs in stdlib.h
date created: Wednesday, January 28th 2026, 2:09:45 pm
date modified: Saturday, February 28th 2026, 12:17:52 pm
---
## `malloc(size)`
You have to calculate your own size, and the chunk of memory it gives you is uninitialized, may be faster than `calloc()` as it doesn't initialize any of the values to anything. Doesn't check if overflows.

## `calloc(n_elements, sizeof_element)`
May be slower than `malloc()` as it needs to zero out `sizeof_element * n_elements` bytes. Needed when you need a spotless buffer. Some implementations check for overflow. 

#C #C/features #memory 