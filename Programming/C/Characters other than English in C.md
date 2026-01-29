This **doesn't** work

```c
char c = "我";
printf("%c", c);
```

`我` is not encoded in `ASCII`, and `ASCII` only stores stuff in 1 byte (8 bits), so this character is likely `UTF-8` or higher. This applies for any characters not in `ASCII`

#C #C/conceptual  