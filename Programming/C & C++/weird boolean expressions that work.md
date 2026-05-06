---
tags: [C, C/features]
title: weird boolean expressions that work
date created: Wednesday, October 22nd 2025, 4:19:01 pm
date modified: Saturday, April 11th 2026, 9:53:49 pm
parent: C & C++
nav_order: 20
---
# weird boolean expressions that work
## `=` (assignment operator) (`:=` in Python)
When you use the assignment operator in a place where a boolean expression is evaluated (like `if`, `while`), it returns (the result of the boolean expression) the value that was assigned to the left item. 

```c
int a = 1;
int b = 2;

a = b; // returns 2 if placed inside an if or while
```

### `++ —-`
When you increment (`++`) or decrement (`—-`), the new value that was changed will be returned. So, using `—-` as an example, `if (n—-)` and `n—-` becomes `0`, the `if` condition will not be satisfied because the value is `0`.

## Arithmetic and bitwise operators
The computed value will be returned. And can also be evaluated as a boolean.

#C #C/features  