```c
int add(int a, int b)
{
	int result = a + b;
	return result;
}
```
Looks right. But this won't work.

The variables declared within a function call are allocated to the stack, and when the function ends (or `return`s), the memory within the stack will be garbage, because the value you allocated isn't propagated anywhere on the stack anymore, therefore, when you try to catch the return value like this: `int add_result = add(1, 2);` it doesn't work. 

`malloc()` is the only workable workaround to it, or using `static`, but that's more dangerous. (see why: [[`static`]])

#C #memory #explanation 