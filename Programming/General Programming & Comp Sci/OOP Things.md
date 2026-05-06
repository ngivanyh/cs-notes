---
tags: [programming, cs]
title: OOP Things
date created: Friday, July 25th 2025, 12:02:18 pm
date modified: Tuesday, May 5th 2026, 9:13:08 pm
parent: General Programming & Comp Sci
nav_order: 8
---
# OOP Things
## `super`


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
### Decorator methods

### Class Variables vs Instance Variables (declared in `__init__`)
|                           | Class Variables                                                                                                                                                                                     | Instance Variables                         |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Scope**                 | Exists in every class                                                                                                                                                                               | Specific to that instance                  |
| **Effects when Modified** | Changes the class variable of every instance of said class[^1]<br><br>[^1]: If you change it from an instance, it will create an instance variable with the same name, shadowing the class variable | Changes the variable of only that instance |


#cs