---
title: vector
date created: Tuesday, July 14th 2026, 2:39:48 pm
date modified: Tuesday, July 14th 2026, 3:01:27 pm
---
# `vector`
## Declaration

```cpp
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
```

## Methods
### `push_back(e)` & `emplace_back(e)`
Both of them push new element `e` to the `vector`. `emplace_back()` being slightly faster.

Long story short, `push_back(e)` will **make a new `vector`** plus one in size to put the new element in the vector, while `emplace_back()` just inserts it at the end.

### `pop_back()`
Removes the last element in the `vector`.

> [!NOTE]
> `vector` doesn't support adding things in the front and removing them in the front, for that look for `queue` or `deque`.

### `empty()`
Checks if the `vector` is empty

### `size()`
Gets the size (length) of the `vector`

#data-structures #cpp #cpp/features 
