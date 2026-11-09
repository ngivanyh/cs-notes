---
title: Monotonic ...
date created: Friday, August 7th 2026, 12:18:36 pm
date modified: Saturday, October 31st 2026, 9:43:27 am
---
# Monotonic ...
Here we'll just cover the two most commonly appearing monotonic data structures used. 

**Monotonicity** in data structures means that a data structure *strictly* maintains a increasing or decreasing order, this way of storing things can be used to find the next greater/smaller element in a sequence

In addition, monotonic data structures such as the monotonic stack can also retain information about the *boundaries* of values, used in problems like [finding the largest area in a histogram](https://github.com/ngivanyh/challenge-solutions/blob/main/largest-rect/largest.py) by recording the indices.

> [!TIP]
> Monotonic data structures usually store **indices**, not values, as it let's you know when an index doesn't fit the order and other things

## 👑 Stack
**Increasing Stack**: `stack.top >= stack.elements`
**Decreasing Stack**: `stack.top <= stack.elements`

Inserting items: Pop until the top of the stack is `<=` or `>=` than the element being added (depending of the order)

Example (Increasing): `arr = [1, 2, 4, 3, 5]`
- Push `1` → Stack: `[1]`
- Push `2` → Stack: `[1, 2]`
- Push `4` → Stack: `[1, 2, 4]`
- Pop `4`, Push `3` → Stack: `[1, 2, 3]`
- Push `5` → Stack: `[1, 2, 3, 5]`

Example (Decreasing): `arr = [1, 2, 4, 3, 5]`
- Push `1` → Stack: `[1]`
- Pop `1`, Push `2` → Stack: `[2]`
- Pop `2`, Push `4` → Stack: `[4]`
- Push `3` → Stack: `[4, 3]`
- Pop `4`, Pop `3`, Push `5` → Stack: `[5]`

## 👑 Queue
Monotonic queues are in practice implemented as [[Deque|deques]], and ==they usually are used to solve problems with a fixed range, instead of dynamic sizes==.

**Increasing Queue**: `queue.back >= queue.elements`
**Decreasing Queue**: `queue.back <= queue.elements`

Example (Increasing): `arr = [1, 2, 4, 3, 5]`
- Push `1` → Deque: `[1]`
- Push `2` → Deque: `[1, 2]`
- Push `4` → Deque: `[1, 2, 4]`
- Pop `4`, Push `3` → Deque: `[1, 2, 3]`
- Push `5` → Deque: `[1, 2, 3, 5]`

Example (Decreasing): `arr = [1, 2, 4, 3, 5]`
- Push `1` → Deque: `[1]`
- Pop `1`, Push `2` → Deque: `[2]`
- Pop `2`, Push `4` → Deque: `[4]`
- Push `3` → Deque: `[4, 3]`
- Pop `4`, Pop `3`, Push `5` → Deque: `[5]`

If you want, I can also rewrite it in **sliding window** form with `push_back`, `pop_back`, and `pop_front`.
#data-structures 