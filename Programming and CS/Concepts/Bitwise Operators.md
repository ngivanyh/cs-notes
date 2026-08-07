---
title: Bitwise Operators
date created: Friday, May 30th 2025, 9:00:54 am
date modified: Thursday, August 6th 2026, 4:59:04 pm
---
# Bitwise Operators
## The Operators
### `&` Bitwise AND:
Compares each bit and returns `1` only if both values have `1` in the same position.

```c
A: 5 // decimal
   101 // binary

B: 4 // decimal
   100 // binary

A & B

    101
&   100
---------
    100 // Only gives you one when both binary numbers have 1 in the same position
```

### `^`  Bitwise XOR:
Exclusive OR: ≒ "difference detector", only returns `1` when the bits are different.

```c
0 ^ 0 = 0 // same, so returns 0
1 ^ 1 = 0 // same, so returns 0

1 ^ 0 = 1 // different, so returns 1
0 ^ 1 = 1 // different, so returns 1
```

```c
C: 3 // decimal
   011 // binary

D: 5 // decimal
   101 // binary

C ^ D

    011
^   101
---------
    110 // Only gives you 1 when both are different from each other
```

### `|` Bitwise OR:
Returns `1` if one of the bits is `1`

```c
E: 6 // decimal
   110 // binary

F: 2 // decimal
   010 // binary

E | F

    110
|   010
---------
    110 // Only returns 1 when either one is 1, because the last bit doesn't have 1 in either E or F, it is 0 
```

### `>>` & `<<` Bitwise Shift:
#### `>>` Right Shift:

```c
9 >> 2

9 -> 0b1001 // binary

>> 2 // shift bits to the right by 2

0b10(01) // will be removed (right shift)

0b1001 >> 2 -> 0b10

0b10 -> 2 // decimal
```

#### `<<` Left Shift:

```c
10 << 2

10 -> 0b1010 // binary

<< 2 // shift bits to left by 2

0b1010(00) // 2 bits will be filled with zero, because of << "2"

0b1010 >> 2 -> 0b101000

0b101000 -> 40 // decimal
```

### `~` Bitwise Complement

```c
10 -> 0b1010 // binary

~10 // bitwise complement

// Rule: 1 becomes 0, and vice versa
~10 -> 0b0101
```

With this, two's complement is really easy, it's just `(~NUM) + 1`.

## Use Cases
### Caution
You shouldn't abuse it for everything, and using bitwise for all the arithmetic might do more harm than good. But if you're doing multiplication/division in powers of 2, they are your friends.

### Even/Odd Checker w/ Bitwise `&`

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

### Fast Halving w/ Bitwise `>>`

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

### Fast Doubler w/ Bitwise `<<`

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
### Swapping Two **Integers**

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

#programming 