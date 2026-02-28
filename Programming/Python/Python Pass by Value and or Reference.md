---
tags: [python]
title: Python Pass by Value and or Reference
date created: Thursday, November 13th 2025, 7:04:39 pm
date modified: Saturday, February 28th 2026, 12:18:28 pm
---
**Useful [reference](https://www.geeksforgeeks.org/python/pass-by-reference-vs-value-in-python/) especially the table on the bottom**

Python, no matter what, will pass the reference to the object (`int`, `str`, `list`, etc are all objects). A way to differentiate is to think of how said object would be defined in C. 

E.g. A `list` would be `type* list_name`, so actually on the low level, it's a pointer to the first item. Therefore, it would be passed by reference, and can be modified in the function. 

An `int` wouldn't, as it is just `int` in C as well, so it's pass by value. (sorta)

#python 