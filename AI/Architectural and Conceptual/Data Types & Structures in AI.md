---
tags: [ai, ai/conceptual]
title: Data Types & Structures in AI
date created: Wednesday, January 28th 2026, 8:10:25 am
date modified: Saturday, July 11th 2026, 10:31:21 pm
parent: Architectural and Conceptual
nav_order: 5
---
# Data Types & Structures in AI
## Data Structures
### Comparing Scalars, Vectors, Matrices, and Tensors

|               | Scalars                                   | Vectors                  | Matrices              | Tensors                                                                       |
| ------------- | ----------------------------------------- | ------------------------ | --------------------- | ----------------------------------------------------------------------------- |
| What they are | Single numerical value (zero dimensional) | Single dimensional array | Two dimensional array | Multi-dimensional array(s) of values (zero dimensions to infinite dimensions) |
Although in PyTorch, a `tensor` can be all four of these.

### How they Apply to an Neural Network
The reason modern neural nets use vectors, matrices, and tensors is to first have more complicated data/inputs. And also because using these data types allows for better leveraging of hardware that can do maths on these much faster than if they were individual scalars. 

But the mechanism of [[Backpropogation|backpropagation]] still apply to them, just on a mutli-dimensional level.

For example, we can use vectors and matrices to speed up operations, even if the input is a bunch of scalars.

But a bunch of scalars as input might be less efficient as they are scattered throughout memory, instead of a contiguous block which is nicer to work with. So, we might bunch them up into these vectors, matrices, and Tensors to also encode more complicated data at the same time. 

Another optimization that arises when we use these higher-dimensional data structures is that we can couple our weights and biases together. Structuring them like this allows us to utilize the capability of specialized or hardware that just does this kind of thing well.

> [!IMPORTANT]
> GPUs are very good at doing arithmetic on matrices and vectors, coming from their typical application of calculating the values of pixels on a display, **which is a grid**.

### Common Configurations of High Dimensional Data Types in AI


## Floating Point Numbers

#ai #ai/conceptual  