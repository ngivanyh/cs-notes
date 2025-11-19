Akin to the Python `*arg` ([[*args and **kwargs]), the `...` in C can signify an variable length argument list, aka a function that takes in practically infinite arguments. 

If we take a look at the declaration of `printf()`, we might see this:

```c
int printf(char *fmt, ...)
```

Note that the `...` notation only appears at the end of the function argument list. The behavior of this notation is defined in `stdarg.h`. A type `va_list` is used to refer to each argument sequentially. Then the `va_start` macro initializes your `va_list` type variable (say we call it `ap`)to the first item in the first unnamed argument. *It must be used once before `ap` is used*. **There must be at least one named argument, in the case of `printf()`, it's `char* fmt`.**

Convesrsely, if you have a `va_start`, `va_end` cleans everything up.

#C #explanation