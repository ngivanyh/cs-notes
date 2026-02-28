---
tags: [C, C/conceptual]
title: Characters other than English in C
date created: Friday, June 27th 2025, 9:58:39 am
date modified: Saturday, February 28th 2026, 9:31:03 pm
---
# Characters other than English in C
This **doesn't** work

```c
char c = "我";
printf("%c", c);
```

`我` is not encoded in `ASCII`, and `ASCII` only stores stuff in 1 byte (8 bits), so this character is likely `UTF-8` or higher. This applies for any characters not in `ASCII`

#C #C/conceptual  