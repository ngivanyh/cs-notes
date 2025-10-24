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
    def wrapper(*args):  # This catches any arguments
        print("before")
        fn(*args)        # Pass them to the original function
        print("after")
    return wrapper       # Return this new function

@my_decorator
def greet(name):
    print(f"hello {name}")

greet("Alice")  # Now this works!
```

When you use `@my_decorator`, Python does this:

```python
greet = my_decorator(greet)
```

So `my_decorator` must return something callable (a function) that replaces the original `greet`. That's why you return `wrapper`.

Also, remember to use `@functools.wraps(fn)`, otherwise your decorator function loses its identity.

#python #python/features #explanation 