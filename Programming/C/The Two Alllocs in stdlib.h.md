---
tags: [C, C/features, memory]
title: The Two Alllocs in stdlib.h
date created: Wednesday, January 28th 2026, 2:09:45 pm
date modified: Monday, April 6th 2026, 8:28:46 am
parent: C
nav_order: 9
---
# The Two Alllocs in stdlib.h
## `malloc(size)`
You have to calculate your own size, and the chunk of memory it gives you is uninitialized, may be faster than `calloc()` as it doesn't initialize any of the values to anything. Doesn't check if overflows.

## `calloc(n_elements, sizeof_element)`
May be slower than `malloc()` as it needs to zero out `sizeof_element * n_elements` bytes. Needed when you need a spotless buffer. Some implementations check for overflow. 

## Reminders
- Do remember to check for `NULL` when the pointer gets spits back out to you.
- Do remember to `free()`.
- Don't use after free.

#C #C/features #memory 