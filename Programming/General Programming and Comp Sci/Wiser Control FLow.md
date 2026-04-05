---
title: Wiser Control FLow
date created: Friday, April 3rd 2026, 10:59:42 pm
date modified: Sunday, April 5th 2026, 10:21:14 pm
tags: [programming]
parent: General Programming and Comp Sci
grand_parent: Programming
nav_order: 12
---
# Wiser Control FLow
## `if` vs `switch`
1. `if` will try each condition and if there is one that it meets, it will jump into that code block and jump to the code after the whole `if`; while `switch` will **keep executing the next case's code after it finds a case that matches** (if you don't add a `break`).
2. `if` can be generally faster when there are not a lot of items, `switch` can offer more speed when there are *a lot* of checks (maybe thousands)

## Wise Logical Control Flow
Whenever there's a boolean expression that needs to be evaluated, `0` is `false` and anything not `0` is `true`, and there is no *actual* need for a boolean to be present anywhere inside the expression.

```python
if a == 0:
# you could really just simplify to
if not a:

# OR...
if a != 0:
# just do this!
if a:

# Another situation
def check_func(*args) -> int
if (out := bool(check_func(a))) and out:
# redundant, just do this
if check_func(a): # if the check is true and the function is designed to push out a non-zero integer because of it
```

`switch` statements are annoying because you have to almost add `break` every time you finish a case, but sometimes, intentionally falling through might lead to a better solution:

> In most programming languages, that is. 

```c
switch (val)
{
    case a:
    case b:
    case c:
    case d:
        // code to execute when val == a/b/c/d
}
```

Just be mindful of the boldfaced part on switch, ==it doesn't keep on checking==.

```c
switch (val)
{
    case a:
        // code for a
        // no break
    case b:
        // after it finishes the code for when val == a, it will execute this part as well
}
```

#programming 