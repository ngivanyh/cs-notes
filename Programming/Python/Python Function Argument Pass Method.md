---
title: Python Function Argument Pass Method
date created: Thursday, November 13th 2025, 7:04:39 pm
date modified: Tuesday, July 7th 2026, 2:19:43 pm
---
# Python Function Argument Pass Method
Python, no matter what, will pass the reference to the object (`int`, `str`, `list`, etc are all objects). A way to differentiate is to think of how said object would be defined in C. 

E.g. A `list` would be `type * list_name`, so actually on the low level, it's a pointer to the first item. Therefore, it would be passed by reference, and can be modified in the function. 

An `int` wouldn't, as it is just `int` in C as well, so it's pass by value. (kind of)

Python is an outlier because of this hybrid function pass mechanism.

#python #memory 