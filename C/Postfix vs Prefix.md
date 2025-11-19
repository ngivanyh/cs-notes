```c
#include <stdio.h>

int main(void)
{
	int i, j = 0;
	printf("i: %d j: %d", i++ + 1, ++j + 1);
	return 0;
}
```

Postfix returns the value of the variable first, then does the increment (or decrement w/ ```i--
``` or ```j--```), and the opposite goes for prefix.

So the value of the printf for ```i++ + 1``` would be 1, but after that, ```i```'s value would be `1` (due to `i++`). And the value for `++j + 1` would be 2, but since the `+ 1` isn't a `+=` ,`++`, or something similar, `j`'s value would be 1 (again, due to `++j`).

#C #explanation #C/conceptual 