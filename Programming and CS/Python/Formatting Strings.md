---
title: Formatting Strings
date created: Tuesday, August 11th 2026, 10:19:56 am
date modified: Tuesday, August 11th 2026, 10:49:45 am
---
# Formatting Strings
## C-Style

```python
from math import pi

print("%.4f" % pi) # prints 3.146 (i.e. round(pi, 4))
print("%d %d" % (1, 2)) # prints 1 2 (must be a tuple after %)
```

This syntax directly uses the C syntax, which you can view [[IO in C#Notation|here]]. Everything is the same down to the left/right padding and precision specification.

This is generally not recommended now as [`f`-strings](#f-strings) are a thing.

## `str.format()` or `format(val, fmt)`


## F-strings

