---
date created: Friday, March 6th 2026, 9:07:15 pm
date modified: Saturday, March 7th 2026, 11:15:25 am
tags: [python, memory]
title: "Python's Pointers"
---
# Python's Pointers
When you print the `__str__` of an `int` say, you get:

```
<method-wrapper '__str__' of int object at 0x102fc6318>
```

Or printing a custom `class` that doesn't have a `__str__` or `__repr__` defined.

Even though Python uses GC (Garbage Collector), it still sometimes will show patterns that will only be understood by people who've learned how manual memory management works.

## Pass-by

#python #memory 