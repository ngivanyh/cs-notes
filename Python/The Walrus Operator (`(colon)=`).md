`:=` Is useful for stuff like:

```python
while (a := input("enter a number: ") && a.isnumeric())
	print("You entered a number")
```

I.E. if you want to declare something that cannot directly be plugged in with the `=` operator. You might want to consider using the walrus operator (in `C` you can just use the `=` assignment operator and then wrap it in parenthesis, but in Python you have to use this).

#python #python/features #explanation 