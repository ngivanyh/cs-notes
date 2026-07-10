---
tags: [C, C/features]
title: goto
date created: Saturday, September 6th 2025, 10:03:57 pm
date modified: Tuesday, June 30th 2026, 10:43:51 am
parent: C & C++
nav_order: 12
---
# `goto`
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

Another use case of `goto` is to write a designated area for cleanup in case of an error, i.e.

```c
MLP * InitMLP(size_t total_layers, size_t * layer_neurons)
{
    float * values = (float *) calloc(total_neurons, sizeof(float));
    if (values == NULL) goto cleanup;    
    
    ... // some code here
    
cleanup:
    free((void *) lns);
    free((void *) values);
    free((void *) activated);
    free((void *) grads);
    free((void *) biases);
    free((void *) weights);
    return NULL;
}
```

#C #C/features  