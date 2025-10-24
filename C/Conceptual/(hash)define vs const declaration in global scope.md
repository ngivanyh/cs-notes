```c
#define NAME VAL
```
When compiled, the compiler will simply just *replace* all instances of `NAME` throughout the program. It has no type, and does not take up any memory (RAM). (preprocessor)

```c
const type name = val;

int main(void)
{
	... /* some code executed */
	
	/* and you can access the variable with */
	extern name ... /* some action to the external value */
}
```
In this version, `name` is a variable, and takes up memory, has a type, and could be manipulatable (by removing the `const`). The [[`extern`]] could be omitted in this situation (same file), but it is still *advisable* to add it (because if you have multiple files, you'd need the `extern`).

#C #explanation 