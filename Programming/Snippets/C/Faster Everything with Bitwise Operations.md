---
tags: [C, snippet]
title: Faster Everything with Bitwise Operations
date created: Friday, May 30th 2025, 9:25:07 am
date modified: Saturday, February 28th 2026, 12:27:24 pm
---
**Applies to other languages with bitwise operations**

## Caution
You shouldn't abuse it for everything, and using bitwise for all the arithmetic might do more harm than good. ~~(e.g. `x * 7` -> `(x << 3) -  x`)~~

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

> ==Note: You can multiply/divide something by powers of two by replacing the number after the operator.==

#C #snippet 