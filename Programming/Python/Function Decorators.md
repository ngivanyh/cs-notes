---
tags: [python, python/features]
title: Function Decorators
date created: Sunday, June 29th 2025, 9:35:43 am
date modified: Monday, April 6th 2026, 8:28:47 am
parent: Python
nav_order: 5
---
# Function Decorators
## Basic Rundown
Since functions can be passed around like variables in Python:

```python
def my_decorator(fn):
    print("before function runs")
    fn()
    print("after function runs")

@my_decorator
def say_hello():
    print("hello world")
```

This `@my_decorator` is just shorthand for:

```python
say_hello = my_decorator(say_hello) # passes a function as the function argument
```

Using a wrapper, you can have the function passed into the decorator have function arguments itself.

```python
def my_decorator(fn):
    def wrapper(*args): # This catches any arguments
        print("before")
        fn(*args) # Pass them to the original function
        print("after")
    return wrapper # Return this new function

@my_decorator
def greet(name):
    print(f"hello {name}")

greet("Ivan") # this prints "before\nhello Ivan\nafter"
```

When you use `@my_decorator`, Python does this:

```python
greet = my_decorator(greet)
```

So `my_decorator` must return something callable (a function) that replaces the original `greet`. That's why you return `wrapper`.

## `functools.wraps()`
Also, remember to use `@functools.wraps(fn)`, otherwise your decorator function loses its identity. By that, it means this: (`__doc__` gets the docstring inside the function, `__name__` for the name)

```python
def a_decorator(func):
    def wrapper(*args, **kwargs):
        """A wrapper function"""
        func()
    return wrapper

@a_decorator
def first_function():
    """This is docstring for first function"""
    print("first function")

@a_decorator
def second_function(a):
    """This is docstring for second function"""
    print("second function")

print(first_function.__name__)
print(first_function.__doc__)
print(second_function.__name__)
print(second_function.__doc__)
```

They will all print:

```
wrapper
A wrapper function
wrapper
A wrapper function
```

You can see that `first_function()` and `second_function(a)` have lost their identities as `first_function()` and `second_function(a)`, rather, they've become `wrapper()`. That's why we need `@functools.wraps(fn)`, that why say if we're debugging, we can know what function called and what caused what. (there are other uses beyond that, but that was one)

#python #python/features  