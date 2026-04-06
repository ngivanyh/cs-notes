---
tags: [python, python/features]
title: Lambda functions (lambda)
date created: Sunday, June 29th 2025, 9:38:33 am
date modified: Monday, April 6th 2026, 8:28:47 am
parent: Python
grand_parent: Programming
nav_order: 3
---
# Lambda functions (lambda)
A Python `lambda` function is a small function that can take any number of arguments, but the return must **only** be in one expression. `lambda` functions are unnamed. 

Essentially, functions like this:

```python
def func(*args):
    return [expression]
```

To this:

```
lambda [args]: [expression]
```

An example:

```python
import random

a = list(range(1, 10001)) # is a list that has 10000 elements starting from 1 and ending in 10000

random.shuffle(a) # randomly shuffles a
```

#python #python/features  