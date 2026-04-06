---
tags: [python, snippet]
title: A Python Program Intended as a Script
date created: Thursday, November 20th 2025, 10:09:50 pm
date modified: Monday, April 6th 2026, 8:28:47 am
parent: Python
nav_order: 1
---
# A Python Program Intended as a Script
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