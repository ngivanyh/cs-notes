---
title: Stack
date created: Tuesday, August 4th 2026, 4:22:00 pm
date modified: Tuesday, August 11th 2026, 3:24:37 pm
---
# Stack
## Python
Just use a normal ol' `list` and call `.pop()`, which'll pop the last item and return the value. And of course, `.append()` for adding elements to the end.

If you want to pop the front or add/remove in the front AND back, please use [[dequeue]]

## C++
### Declaration

```cpp
#include <stack>

/* 1 */
stack<T> s; // empty stack

/* 2 */
stack<T> s;
v.resize(n); // make vector have n elements

/* 3 */
vector<T> v(n); // shorthand for 2

/* 4 */
vector<int> v = {1, 2, 3}; // direct assignment

/* 5 */
vector<int> v(n, 1); // fill this vector with n 1's
// no second argument (like 3) will fill with 0's
```

### Methods
#### `push(e)`
Pushes an element to the top of the `stack`

#### `pop()`
Removes the item at the top of the `stack`

> [!IMPORTANT]
> You cannot call `.pop()` or `.top()` when the `stack` is empty (it's undefined behavior), always check with `.empty()`

#### `top()`
Gets the top element of the `stack`

#### `empty()`
Checks if the `vector` is empty

#### `size()`
Gets the size (length) of the `stack`


#data-structures #cpp #cpp/features #python 
