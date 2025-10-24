**This file contains both explanation for the `extern` keyword and also just dealing with external files in `C` that need to be stringed together.**

#### `extern` variables and functions:
- Not strictly necessary
- The *initialization* happens in the source file, so in the other programs you're *declaring* it as an external variable, it doesn't reserve any extra space to accommodate. 
- If you have an `extern` variable used in your file, and that variable is an array. They size need not to be declared. (E.g. *file1*: `int arr[SIZE]`, *file2*: `extern int arr[]`)
- Only one *definition* is allowed of that external variable/function.
- TL;DR -> You can **declare** external variables with `extern`, and it can help discern the internal variables, from the external.

#### Compilation of Multifiled Programs:

`cc`:

```
$ cc abc.c def.c ghi.c
```

#C #explanation #C/features
