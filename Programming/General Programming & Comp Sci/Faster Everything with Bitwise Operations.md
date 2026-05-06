---
tags: [C, snippet]
title: Faster Everything with Bitwise Operations
date created: Friday, May 30th 2025, 9:25:07 am
date modified: Wednesday, May 6th 2026, 2:43:46 pm
parent: General Programming & Comp Sci
nav_order: 6
---
# Faster Everything with Bitwise Operations
**Applies to other languages with bitwise operations**

## Caution
You shouldn't abuse it for everything, and using bitwise for all the arithmetic might do more harm than good. But if you're doing multiplication/division in powers of 2, they are your friends.

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

> [!NOTE]
> `a << b` multiplies `a` by $2^b$; `a >> b` divides `a` by $2^b$

#C #snippet 