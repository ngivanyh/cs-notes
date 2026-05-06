---
tags: [programming]
title: Cycle
date created: Tuesday, January 20th 2026, 4:45:03 pm
date modified: Wednesday, May 6th 2026, 2:45:29 pm
parent: General Programming & Comp Sci
nav_order: 3
---
# Cycle
Cycles through items in a list, rolls over.

```python
l = [1, 2, 3, ...]

# access next item
l[(current_index + 1) % len(l)]

# access previous item
l[(current_index - 1 + len(l)) % len(l)]
```

The `%` (modulo) operator is not just useful for checking if a number is a multiple of something, it's also useful for cycling/repeating things.

#programming 