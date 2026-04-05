---
tags: [python, snippet]
title: Cycle
date created: Tuesday, January 20th 2026, 4:45:03 pm
date modified: Sunday, April 5th 2026, 10:21:15 pm
parent: Python
grand_parent: Snippets
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

#python #snippet 
