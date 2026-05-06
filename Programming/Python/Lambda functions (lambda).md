---
tags: [python, python/features]
title: Lambda functions (lambda)
date created: Sunday, June 29th 2025, 9:38:33 am
date modified: Saturday, April 11th 2026, 9:53:49 pm
parent: Python
nav_order: 5
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