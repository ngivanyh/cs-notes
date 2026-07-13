---
title: Wiser Control FLow
date created: Friday, April 3rd 2026, 10:59:42 pm
date modified: Thursday, July 9th 2026, 4:36:45 pm
---
# Wiser Control FLow
## `if` vs `switch`
1. `if` will try each condition and if there is one that it meets, it will jump into that code block and jump to the code after the whole `if`; while `switch` will **keep executing the next case's code after it finds a case that matches** (if you don't add a `break`).
2. `if` can be generally faster when there are not a lot of items, `switch` can offer more speed when there are *a lot* of checks (maybe thousands)

## Wise Logical Control Flow
### Implicit Boolean Expressions
Whenever there's a boolean expression that needs to be evaluated, `0` is `false` and anything not `0` is `true`, and there is no *actual* need for a boolean to be present anywhere inside the expression.

```python
if a == 0:
# you could really just simplify to
if not a:

# OR...
if a != 0:
# just do this!
if a:
```

Here is a list things that are also interpreted as `false`:
- `NULL`
- `None` (Python)
- `undefined`
- `\0` (NUL character)
- `0.0`

### Using the Return Characteristic

```python
# Another situation
def check_func(*args) -> int
if out := bool(check_func(a)):
# redundant, just do this
if check_func(a): # if the check is true and the function is designed to push out a non-zero integer because of it
```

Those are the return values of the functions, however, other operators also can return values when computed.

```c
while (a--)
    printf("%d ", a);
/* if a is 5, prints: 4 3 2 1 0 */
    
if (b = func(c))
    ;
```

As you can see, since we know arithmetic operators like `++`, `--` or `=` return values, we can use that to check stuff.

### Annoyances of `switch`
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

Just be mindful—==it doesn't keep on checking==—when you have a case that doesn't have `break` that runs.

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

### Strategic Control Flow Placement
Using premature returns to reduce nesting:

```python
def a(b) -> int:
    if cond:
        return 1
    # we don't need else!
    return -1
    
    # obviously, the pythonic way is to do this
    return 1 if cond else -1
```

The next instance is best left with an example:

```cpp
#include <iostream>

int main(void)
{
    int length, m, cm;
    std::cin >> length; // length in centimeters
    
    if (m = length / 100)
        std::cout << m << "公尺";
    
    if (cm = length % 100)
        std::cout << cm << "公分";
    
    std::cout << '\n';
    return 0;
}
```

One way to approach that would have been to set `if` statements for when there is a meter count AND when there is a centimeter count, when there is just a meter count, and when there is just a centimeter count. But by using this method, it reduces and indent and just looks cleaner without the `if`, `else if`, `else` chain. In Python/JavaScript, there is a `finally` keyword that does exactly that after a loop or any control flow finishes.
### Never Nesting
Not exactly "never", but it does make you aware to the number of indents you're putting. There are two ways to reduce nesting:
- **Inversion**: Inverting boolean expressions, say `if a is not None and b` becomes `if a is None or not b`, you invert what you're checking. Instead of seeing if something meets the requirements, you "jettison" out the invalid situations first
- **Extraction**: Extract the complicated checks and boolean expressions to a function, outside of the current code

#programming 