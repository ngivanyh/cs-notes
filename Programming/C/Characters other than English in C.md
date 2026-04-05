---
tags: [C, C/conceptual]
title: Characters other than English in C
date created: Friday, June 27th 2025, 9:58:39 am
date modified: Sunday, April 5th 2026, 10:21:14 pm
parent: C
grand_parent: Programming
nav_order: 2
---
# Characters other than English in C
This **doesn't** work

```c
char c = "我";
printf("%c", c);
```

`我` is not encoded in `ASCII`, and `ASCII` only stores stuff in 1 byte (8 bits), so this character is likely `UTF-8` or higher. This applies for any characters not in `ASCII`

#C #C/conceptual  