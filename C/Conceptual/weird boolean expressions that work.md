### `=` (assignment operator)
When you use the assignment operator in a place where a boolean expression is evaluated (like `if`, `while`), it returns (the result of the boolean expression) the value that was assigned to the left item. 

```c
int a = 1;
int b = 2;

a = b; // returns 2 if placed inside an if or while
```

### `++ —-`
When you increment (`++`) or decrement (`—-`), the new value that was changed will be returned. So, using `—-` as an example, `if (n—-)` and `n—-` becomes `0`, the `if` condition will not be satisfied becuase the value is `0`.

### Arithmetic and bitwise operators
The computed value will be returned. And can also be evaluated as a boolean.