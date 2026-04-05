---
tags: [cs]
title: Arrays vs Pointers
date created: Wednesday, January 28th 2026, 9:39:40 pm
date modified: Sunday, April 5th 2026, 10:21:14 pm
parent: General Programming and Comp Sci
grand_parent: Programming
nav_order: 1
---
# Arrays vs Pointers
Arrays and pointer have a lot in common. They are basically one with the other in C. But there are differences.

An ==**array**== is a contiguous chunk of values stored in memory. While a ==**pointer**== is a address to a specific place in memory. 

So, the saying of not being able to get the size of a array in C is not totally wrong. But in the example here you can actually get the array size:

```c
int arr[3];
printf("%lu", sizeof(arr)); // prints 12, meaning 12 bytes
```

So, you still can't get the array size from pointers, because they can point to anything; random addresses, array elements, `NULL`, single integers, etc. 

But when you pass an array into a function, you are automatically passing the **pointer** to the first element of the array. So, a lot of times, arrays will *decay* into pointers. 

#cs