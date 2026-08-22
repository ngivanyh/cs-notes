---
title: Queues
date created: Friday, August 7th 2026, 12:23:20 pm
date modified: Tuesday, August 11th 2026, 2:59:03 pm
---
# Queues
## Python
Just use the `dequeue` from collections, and you have a queue if you don't use it for deletions at the end and insertions from the start.

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

↓

```python
from collections import deque as queue # IMPORTANT! the spelling is "deque"

q = queue([1, 2, 3, 4, 5])

q.append(6)
q.extend([7, 8, 9])
q.popLeft()

# special fun stuff
q.rotate(1) # rotates elements by 1
q.reverse()
```
## C++

#data-structures 