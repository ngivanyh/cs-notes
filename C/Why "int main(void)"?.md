Due to the unstandardized of nature of C back then, function prototypes didn't have to be the same as the actual function definition. 
```c
/* Back then */
void somefunc() /* see how there're no function arguments */

int main(void)
{
	... /* some code */
}

void somefunc(int a, ... ) /* but there are function arguments now */
{
	... /* function body */
}
```
As you can see, the declaration on the top of the file (`void somefunc()`) is different from the one below (`void somefunc(int a, ...)`), although they are the same function. Therefore, in an effort to maintain some level of backwards compatibility when C was eventually standardized, they kept the fact that empty parenthesis in a function (`()`) could imply that this function takes in an *undefined amount* of arguments.

But by passing `void` into the parenthesis, it tells the compiler that the function *takes no arguments*. Hence why, it is considered good practice to put `void` into the function arguments if the function takes none.

✅: (since `func_name` doesn't take any arguments, it should just be void in the `()`s)
```c
return_type func_name(void);

int main(void)
{
	... /* code executed here */
}

return_type func_name(void)
{
	... /* function body */
}
```

#C #C/conceptual #explanation 
