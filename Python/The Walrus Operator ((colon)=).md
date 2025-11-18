`:=` Is useful for stuff like:

```python
while (a := input("enter a number: ") and a.isnumeric())
	print("You entered a number")
```

I.E. if you want to declare something that cannot directly be plugged in with the `=` operator. You might want to consider using the walrus operator (in `C` you can just use the `=` assignment operator and then wrap it in parenthesis, but in Python you have to use this).

In Python `=` is a *statement*, and it doesn't really return the value the variable stored. But the `:=` is an *expression*, it can return the value the variable just stored, just like in C, using the `=` operator in `while`s, `if`s, etc. 

#python #python/features #explanation 