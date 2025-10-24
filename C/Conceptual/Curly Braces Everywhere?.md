It is actually not required if you only have one statement (or expression) inside control flow operators (like `while`, `for`, `if`, etc).

So it is perfectly valid to do something like this
```c
#include <stdio.h>

int main(void)
{
	int i = 0;
	
	if (i == 0)
		printf("i is zero");
	else
		printf("i isn't zero");

	return 0;
}
```
This program obviously prints `i is zero`, but it is merely an example of the exemption of `{}`s in the `if` among other control flow statements.
```c
#include <stdio.h>

int main(void)
{
	int j = 0;
	
	for (int i = -10; i < someValue; ++i)
		if (j > i)
		{
			printf("j is greater than i");
			i++;
		}

	return 0;
}
```
This works because there is only one statement inside the `for` loop, which is `if`, but the if has multiple statements, including the `printf` and the `i++`, so the `{}`s are required.

#C #explanation 