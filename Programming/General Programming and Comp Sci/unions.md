Kinda like a `enum`, but instead of being able to have multiple different values under a same `enum`. You can STORE values of different types in one `union`.

```c
union {
	int integer_val;
	float floating_point_val;
	char* string_val;
} eg;
```

As you can see, this `union` can at one time store either a value of type `int`, `float`, or `char*` (aka string). Members of `union`s are accessed via the same `.`‘s and `->`’s for `struct`. Programmer’s responsibility to keep track of whatever’s in the union at the current moment. 

When initializing a new variable that’s something that’s a part of a `union`, the type of the first thing defined in the `union` will be used as the sole initializing type for that variable.

#programming 