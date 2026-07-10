---
tags: [C, snippet]
title: Faster Everything with Bitwise Operations
date created: Friday, May 30th 2025, 9:25:07 am
date modified: Wednesday, July 8th 2026, 3:01:40 pm
parent: General Programming & Comp Sci
nav_order: 3
---
# Better Everything with Bitwise Operations
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
## Swapping Two **Integers**

Best if they are both integers, using this method may be in vain because your compiler might do this optimization for you.

```c
#include <stdio.h>

int main(void)
{
    int a = 5;
    int b = 4;

    a ^= b;
    b ^= a;
    a ^= b;

    // now a = 4, b = 5

    return 0;
}
```

**Explanation**:
1. `a ^= b`: Gets the difference of `a` and `b`
2. `b ^= a`: Makes up the difference between `b` and `a`, making `b` `a`'s original value
3. `a ^= b`: Uses that difference to recover `b`'s original value

Replaces the traditional method of using a temporary value and storing one variable in it

#C #snippet 