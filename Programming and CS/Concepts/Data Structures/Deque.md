---
title: Deque
date created: Friday, August 7th 2026, 12:20:18 pm
date modified: Saturday, November 7th 2026, 9:06:25 am
---
# Deque
Even though they are **double-ended ==queues==**, they are usually written as "deque".

## Python

```python
from collections import deque # IMPORTANT! the spelling is "deque"

dq = deque([1, 2, 3, 4, 5])

# list like methods, manipulates the right side
dq.append(6)
dq.extend([7, 8, 9])
dq.pop()

# with a left attached, maniuplates the left side
dq.appendleft(0)
dq.popleft()

# special fun stuff
dq.rotate(1) # rotates elements by 1
dq.reverse()
```

## C++

```cpp
#include <deque>

// initialization
deque<int> dq;

// append element to the left side (back)
dq.push_back(5);

// append element to the right side (front)
dq.push_front(5);

// pop element on the left side (back)
dp.pop_back();

// pop element on the right side (front)
dq.pop_front();

// get size (amount of elements)
dp.size();

// check if empty
dq.empty();
```

#data-structures 