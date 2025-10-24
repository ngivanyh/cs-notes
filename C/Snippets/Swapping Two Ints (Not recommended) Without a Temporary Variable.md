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

## ONLY WORKS WITH INTEGERS AND IS NOT RECOMMENDED. IF YOU REALLY NEED TO DO THIS, ALSO MAKE SURE THEY DO NOT POINT TO THE SAME MEMORY ADDRESS

## Explanation: [[Swapping Ints with Bitwise XOR]]
