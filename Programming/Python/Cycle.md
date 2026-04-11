---
tags: [python, snippet]
title: Cycle
date created: Tuesday, January 20th 2026, 4:45:03 pm
date modified: Saturday, April 11th 2026, 9:53:49 pm
parent: Python
nav_order: 4
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

#python #snippet 
