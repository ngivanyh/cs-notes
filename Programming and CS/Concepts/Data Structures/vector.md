---
title: Vector
date created: Tuesday, July 14th 2026, 2:39:48 pm
date modified: Saturday, October 31st 2026, 9:30:51 am
---
# Vector

```cpp
#include <vector>

/* 1 */
vector<T> v; // empty vector

/* 2 */
vector<T> v;
v.resize(n); // make vector have n elements

/* 3 */
vector<T> v(n); // shorthand for 2

/* 4 */
vector<int> v = {1, 2, 3}; // direct assignment

/* 5 */
vector<int> v(n, 1); // fill this vector with n 1's
// no second argument (like 3) will fill with 0's

// both add an element to the back, the latter is faster
v.push_back(1);
v.emplace_back(2);

// removes an element from the back
v.pop_back()

// check if empty
v.empty()

// get the length
v.size()
```

### `push_back(e)` vs `emplace_back(e)`
Both of them push new element `e` to the `vector`. `emplace_back()` being slightly faster.

Long story short, `push_back(e)` will **make a new `vector`** plus one in size to put the new element in the vector, while `emplace_back()` just inserts it at the end.

#data-structures #cpp #cpp/features 
