```python
def main():
	...

if __name__ == "__main__":
	main()
```

It guarantees this program is intended to be ran as a script. (because it `__name__ == "__main__"`)

If `multiprocessing` is used, it must be ran as a script, hence the interpreter will tell you to add this statement.

#python #snippet 