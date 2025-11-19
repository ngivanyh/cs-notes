Plain snippet: [[Swapping Two Ints (Not recommended) Without a Temporary Variable]]
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

`a ^= b`: Gets the difference of `a` and `b`
`b ^= a`: Makes up the difference between `b` and `a`, making `b` `a`'s original value
`a ^= b`: Uses that difference to recover `b`'s original value

#C #snippet #explanation 