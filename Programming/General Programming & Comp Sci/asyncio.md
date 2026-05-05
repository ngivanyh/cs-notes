---
tags: [programming]
title: asyncio
date created: Tuesday, January 20th 2026, 11:36:41 am
date modified: Saturday, April 11th 2026, 9:53:49 pm
parent: General Programming & Comp Sci
nav_order: 14
---
# asyncio
The name of the package used in Python. It is used for **Asynchronous Programming**, it and the JS equivalent will be used to exemplify async programming.

When we slap the `async` keyword onto a function:

```python
async def func(*args):
    # does things here
    ...
```

or 

```js
async function func(args, ...) {
    // does things here
    ...
}
```

We are saying "this function can be ran asynchronously, in laymen's terms, the CPU doesn't need to wait until it finishes".

So when we do this:

```python
# code above
func(args)
# code below
```

The program starts running that function and just leaves it at that, it goes on to the next lines of code.

But what happens when we `await`?

```js
await func(args);
```

The program "waits" for this function to finish before executing more code below it, but during this time, the CPU does other things it might need to tend to. So, this function doesn't block the whole CPU thread from doing other things, because when we have a synchronous program and it's waiting for something, the whole thread is just there waiting for the task to finish so it can move on.

`async` frees the CPU to do other stuff until the function finishes and it can go back to running the next few lines in the program. It's not parallelism. 

#programming  