## Stack:
- Last in, first out (LIFO). Whatever functions/memory on the **call stack** gets deallocated this way, paves the way for [recursion]()
- Automatic deallocation after the completion of a function ([related](obsidian://open?vault=Computers%20-%20Infinity%20Stones&file=C%2FConceptual%2FPassing%20Variables%20Declared%20within%20Function%20as%20Return%20Variables))
- Functions and its associated variables are allocated here
- Limited space, that's why if you have too many functions and variables within them, you'll run out of space in the stack, hence "stack overflow error"
- Memory is allocated in contiguous blocks, and to visualize, they are "stacked" on top of each other. Newer ones on top, older ones on the bottom. (LIFO)

## Heap:
- **NOT** freed automatically (so use `free()`)
- Dynamic, there's no limit (except for how much memory you have left for the heap ofc)
- Visualized like a pool
- `malloc()` is allocated here

#os #os/general #memory