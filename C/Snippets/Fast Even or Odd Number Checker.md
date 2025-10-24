
```c
#include <stdio.h>

int main(void)
{
	int a;
	scanf("%d", &a);

	if (a & 1) // faster than a % 2 == 1 because & is a native CPU operation
		printf("a is odd");
	else
		printf("a is even");
}
```
