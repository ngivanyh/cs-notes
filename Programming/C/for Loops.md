---
tags: [C, C/conceptual]
title: for Loops
date created: Friday, June 27th 2025, 9:55:58 am
date modified: Saturday, February 28th 2026, 12:17:49 pm
---
```c
for (int i = 0; i < val; ++i)
{
	// loop body goes here
}
```

After the first iteration, `++i` gets executed, then `i < val` gets evaluated, if `i < val` is `false` then we exit the loop, if it's true, the loop re-executes.

On the initialization (`int i = 0`), the condition gets evaluated (`i < val`), then the loop body gets ran.

#C  #C/conceptual 