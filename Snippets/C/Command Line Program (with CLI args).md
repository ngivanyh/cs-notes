```c
#include <stdio.h>

int main(int argc, char **argv)
{
	if (argc < REQ_ARGS)
	{
		printf("Usage: <name> <args>");
		return 1;
	}

	... /* code goes here */
}
```
