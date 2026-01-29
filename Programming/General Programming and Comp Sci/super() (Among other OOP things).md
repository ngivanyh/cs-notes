### `super()`

### Inheritance
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
### Private/Public fields

### (Python) Decorator methods

#programming 