---
tags: [python, python/features]
title: del
date created: Wednesday, July 2nd 2025, 4:46:47 pm
date modified: Saturday, February 28th 2026, 12:18:25 pm
---
`del`etes objects, since about everything in Python is a object, from `str`s, `int`s, `float`s, `list`s, etc. It is basically the incinerator in Python. But it doesn't **deallocate** memory, it ***==removes a reference==*** to the thing you're deleting, it only frees stuff because you've removed every last reference of that thing your deleting, then the garbage collector will pretty soon realize it can free that memory, therefore the memory is freed. 

One use of the `del` keyword is to delete parts of an array. But doing that shouldn't be done WHILE the array is being iterated/operated on, and there is also a `.remove()` (put in the VALUE of thing the thing you're trying to remove, but it won't remove all duplicates). 

#python #python/features  