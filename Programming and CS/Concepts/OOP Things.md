---
title: OOP Things
date created: Friday, July 25th 2025, 12:02:18 pm
date modified: Monday, August 10th 2026, 9:59:25 am
---
# OOP Things
## Inheritance
When a class **inherits** some parent class, all the attributes and methods that belong to the parent become a part of the child. But when you redefine the same attributes and methods, e.g.

```python
class Car:
    def honk():
	    print("honk")
    
class BMW(Car):
    def honk():
        for i in range(3):
    	    super().honk()
    	    print(" " if i < 2 else "", end="")
```

you will see the `honk()` method get redefined, so when you call `BMW.honk()` it will print `honk honk honk` rather than the original `honk`

Inheritance is useful when a class extends the original, and when you have a lot of classes that extend the original, you might be able to save lines of code because you don't have to redefine the same classes over and over again.

If your class inherits from a *single* parent, it's **single inheritance**; from multiple, it's **multiple inheritance**.

## `super`
Classes can inherit things from classes, and `super`/`super()` (language-dependent), can essentially call the stuff in the parent class. But `super()` can have two arguments passed to it, one is the subclass, the other is an object that is an instance of the class (e.g. `self`).

> [!NOTE]
> Just calling `super()` **should** be enough for the most part. (Python)

## Private, Public, Protected fields


## Python-specific
### Decorator methods

### Class Variables vs Instance Variables (declared in `__init__`)
|                           | Class Variables                                                                                                                                                                                     | Instance Variables                         |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Scope**                 | Exists in every class                                                                                                                                                                               | Specific to that instance                  |
| **Effects when Modified** | Changes the class variable of every instance of said class[^1]<br><br>[^1]: If you change it from an instance, it will create an instance variable with the same name, shadowing the class variable | Changes the variable of only that instance |

### Special Methods

```python
__add__
__sub__
__mul__
__truediv__
__pow__
__neg__
__repr__
__str__
__radd__
__rsub__
__rmul__
__rtruediv__
__call__
```

Say you have a class `c`, and two variable of type `c` (let's call them `a` and `b`) if you do the following, it won't really have any desired result.

```python
class c:
    def __init__(self):
	    ...
    ...

a = c()
b = c()
```

```python
a + b # error!
a - b # error!
a * b # error!
a / b # error!
a ** b # error!
-a # error!
a + 2 # error!
6 * b # error!
print(a) # doesn't really print anything useful
```

These special class methods tell Python what to do when you do the operations above. 

[The full list of special class methods](https://docs.python.org/3/reference/datamodel.html#specialnames)

#cs #python #python/features 