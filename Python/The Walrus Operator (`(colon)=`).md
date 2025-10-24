`:=` Is useful for stuff like:

```python
while (a := input("enter a number: ") && a.isnumeric())
	print("You entered a number")
```

I.E. if you want to declare something that cannot directly be plugged in with the `=` operator. You might want to consider using the walrus operator.

#python #python/features #explanation 