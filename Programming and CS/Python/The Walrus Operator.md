---
title: The Walrus Operator
date created: Sunday, June 29th 2025, 9:32:49 am
date modified: Saturday, April 11th 2026, 9:53:49 pm
---
# The Walrus Operator
`:=` Is useful for stuff like:

```python
while (a := input("Enter a number: ") and a.isnumeric())
    print("You entered a number")
```

I.E. if you want to declare something that cannot directly be plugged in with the `=` operator. You probably should consider the walrus operator (in `C` you can just use the `=` assignment operator and then wrap it in parenthesis, but in Python you have to use this).

In Python `=` is a *statement*, and it doesn't really return the value the variable stored. Whereas the `:=` is an *expression*, it can return the value the variable just stored, just like in C, using the `=` operator in `while`s, `if`s, etc. 

The walrus operator doesn't support multi-variable assignments like `a, b = 1, 2`.

Supported in Python 3.8 and above.

#python #python/features  