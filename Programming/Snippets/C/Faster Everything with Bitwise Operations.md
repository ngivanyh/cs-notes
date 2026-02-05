**Applies to other languages with bitwise operations**
## Even/Odd Checker w/ Bitwise `&`

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
		
	return 0;
}
```

Replaces `n % 2`.
## Fast Halving w/ Bitwise `>>`

```c
#include <stdio.h>

int main(void)
{
	int a;
	scanf("%d", &a);

	printf("Half of a: %d", a >> 1);
		
	return 0;
}
```

Replaces `n / 2` or `n // 2`(Python Integer Division/Floor Division)

## Fast Doubler w/ Bitwise `<<`

```c
#include <stdio.h>

int main(void)
{
	int a;
	scanf("%d", &a);

	printf("Double of a: %d", a << 1);
		
	return 0;
}
```

#C #snippet #C/features 