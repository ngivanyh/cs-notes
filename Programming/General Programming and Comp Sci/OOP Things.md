---
tags: [programming, cs]
title: OOP Things
date created: Friday, July 25th 2025, 12:02:18 pm
date modified: Saturday, April 11th 2026, 9:53:49 pm
parent: General Programming and Comp Sci
nav_order: 6
---
# OOP Things
## `super()`


## Inheritance
When a class **inherits** some parent class, all the attributes and methods that belong to the parent become a part of the child. But when you redefine the same attributes and methods, e.g.

```python
class Car:
    def honk():
	    print("honk")
    
class BMW(Car):
    def honk():
	    print("honk honk honk")
```

you will see the `honk()` method get redefined, so when you call `BMW.honk()` it will print `honk honk honk` rather than the original `honk`

Inheritance is useful when a class extends the original, and when you have a lot of classes that extend the original, you might be able to save lines of code because you don't have to redefine the same classes over and over again.

## Private, Public, Protected fields


## Python-only
### (Python) Decorator methods

### Declaring Properties in a method (like `__init__`) vs. directly inside the `class`


#cs