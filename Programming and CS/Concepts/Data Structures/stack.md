---
title: Stack
date created: Tuesday, August 4th 2026, 4:22:00 pm
date modified: Thursday, November 5th 2026, 8:09:13 pm
---
# Stack
## Python
Just use a normal ol' `list` and call `.pop()`, which'll pop the last item and return the value. And of course, `.append()` for adding elements to the end.

If you want to pop the front or add/remove in the front AND back, please use [[Deque]]

To access the top use `list[-1]`, beware that the list must have elements in it, otherwise it's an error.

## C++
### Declaration

```cpp
#include <stack>

// stack declaration
stack<T> s;

// put an element on top of the stack
s.push(1);

// remove the top element
s.pop();

// get the top element
s.top();

// check if stack is empty
s.empty();

// get the length of the stack
s.size();
```

> [!IMPORTANT]
> You cannot call `.pop()` or `.top()` when the `stack` is empty (it's undefined behavior), always check with `.empty()`

#data-structures #cpp #cpp/features #python 
