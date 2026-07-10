---
tags: [programming, memory]
title: Passing Variables Declared within Function as Return Variables
date created: Tuesday, July 1st 2025, 10:32:52 am
date modified: Wednesday, May 6th 2026, 2:20:58 pm
parent: General Programming & Comp Sci
nav_order: 12
---
# Passing Variables Declared within Function as Return Variables

```c
int * slice_arr(int * arr, int start, int end)
{
    int * slice_arr[LENGTH];
    ... // slicing goes here
    return slice_arr;
}
```

Looks right. But this won't work.

The variables declared within a function call are allocated to the stack, and when the function ends (or `return`s), the memory within the stack will be garbage, because the value you allocated isn't propagated anywhere on the stack anymore, therefore, when you try to catch the return value like this: `int * sliced = slice_arr(arr, 1, 2);` it doesn't work. 

`malloc()` is the only workable workaround to it, or using [[static]], but that's more dangerous.

#programming  #memory  