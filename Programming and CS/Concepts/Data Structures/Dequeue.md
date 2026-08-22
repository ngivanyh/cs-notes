---
title: Dequeue
date created: Friday, August 7th 2026, 12:20:18 pm
date modified: Tuesday, August 11th 2026, 2:56:24 pm
---
# Dequeue
## Python

```python
from collections import deque # IMPORTANT! the spelling is "deque"

dq = deque([1, 2, 3, 4, 5])

# list like methods, manipulates the right side
dq.append(6)
dq.extend([7, 8, 9])
dq.pop()

# with a left attached, maniuplates the left side
dq.appendLeft(0)
dq.popLeft()

# special fun stuff
dq.rotate(1) # rotates elements by 1
dq.reverse()
```

#data-structures 