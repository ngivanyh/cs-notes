`static` variables exist in the data portion of a program. They are only initialized once, and they can persist throughout the execution of the program. They are also ***strictly*** internal, and they only exist in the scope they were defined in. For example:

```c
#include <stdio.h>

void add_numbers()
{
    static a = 10;
    int b = 10;
    
    a += 5;
    b += 5;
    
    printf("a: %d, b: %d", a, b); 
}

int main(void)
{
    add_numbers();
    add_numbers();
    add_numbers();
    
    return 0;
}
```

The output will be:

```c
a: 15, b: 15
a: 20, b: 15
a: 25, b: 15
```

So they are useful for fixes circumventing the fact that you can't return pointers. But they aren't thread-safe (safe from other threads of execution, if your program is multithreaded), so just use `malloc()`


#C #C/features #explanation 