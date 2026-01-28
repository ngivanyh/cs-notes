You basically setup a identifier (or key, whatever you like to call it) and when the program reaches a `goto`, the program execution will jump to the place you've setup that identifier/key. It's not that useful, and can cause your program to be hard to debug if you abuse it, but it may be useful when you're in a big loop and breaks aren't sufficient to exit the loop (or they can't exit quickly, because you'd have to spam `break`). The `goto` is essentially assembly's `JMP`.

This situation might be one where using `goto` is better than just using `break`s.
```c
while (...) {
    for (...) {
        for (...) {
            ...
            if (something_happens) {
                goto someplace
            }
        }
    }
}

someplace:
    ... // some code to be executed here
```

#C #C/features #explanation 