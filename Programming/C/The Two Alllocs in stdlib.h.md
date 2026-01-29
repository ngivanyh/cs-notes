## `malloc(size)`
You have to calculate your own size, and the chunk of memory it gives you is uninitialized, may be faster than `calloc()` as it doesn't initialize any of the values to anything. Doesn't check if overflows.

## `calloc(n_elements, sizeof_element)`
May be slower than `malloc()` as it needs to zero out `sizeof_element * n_elements` bytes. Needed when you need a spotless buffer. Some implementations check for overflow. 