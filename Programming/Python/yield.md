---
tags: [python, python/features]
title: yield
date created: Wednesday, July 2nd 2025, 4:46:22 pm
date modified: Wednesday, July 8th 2026, 3:03:27 pm
parent: Python
nav_order: 13
---
# yield
Used to create generators/iterators (there's a small difference, but it's minor) (e.g., `enumerate`) (`range(start, stop, step)` **is not a iterator**, it is more of a function to generate a string of numbers from `start` to `stop - 1`, incrementing my `step` each time).

Since the function with `yield` is now a iterator, the `next()` function applies to it. (get the next value from the iterator)

```python
def fun(m):
    for i in range(m):
        yield i  

for n in fun(5):
    print(n)
```

You can think of it as like a `return` that doesn't make the function exit. When you call the function, the function will `yield` the expression after the `yield` keyword.
## Advantages:
- Infinite sequences (you can create a function that yields the numbers in a fibonacci sequence for example)
- Since `yield` allows you to "pause"/resume the function, it's good for async programming
- Fine-grained control over iteration
- Memory-efficient, everything comes when you want it to, and not all at once too
- The state inside the function with `yield` retains the state it was on.

#python #python/features  