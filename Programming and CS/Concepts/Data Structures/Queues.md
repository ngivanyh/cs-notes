---
title: Queues
date created: Friday, August 7th 2026, 12:23:20 pm
date modified: Monday, November 9th 2026, 7:44:05 pm
---
# Queues
## Python
Just use the `deque` from collections, and you have a queue if you don't use it for deletions at the end and insertions from the start.

```python
from collections import deque # IMPORTANT! the spelling is "deque"

...
```

(See [[Deque]] for more)

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
### Normal Queue

```cpp
#include <queue>

// queue declaration
queue<int> q;

// push element to queue
q.push(5);

// pop element from queue
q.pop();

// check if queue is empty
q.empty();

// check the element in the front of the queue
q.front();
```

### Priority Queue

#data-structures 