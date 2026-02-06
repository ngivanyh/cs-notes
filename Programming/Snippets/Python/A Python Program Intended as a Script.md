```python
def main():
	...

if __name__ == "__main__":
	main()
```

It guarantees this program is intended to be ran as a script. (because it `__name__ == "__main__"`)

If `multiprocessing` is used, it must be ran as a script, hence the interpreter will tell you to add this statement.

This pattern also provides another advantage: you don't have to implement all the functions you want to use in `main()` before `main()`. A little creature comfort coming from C function declarations.

#python #snippet 