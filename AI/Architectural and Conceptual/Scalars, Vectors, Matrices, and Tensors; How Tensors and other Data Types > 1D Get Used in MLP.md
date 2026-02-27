## Scalars, Vectors, Matrices, and Tensors—A comparison

|               | Scalars                                   | Vectors                  | Matrices              | Tensors                                                                       |
| ------------- | ----------------------------------------- | ------------------------ | --------------------- | ----------------------------------------------------------------------------- |
| What they are | Single numerical value (zero dimensional) | Single dimensional array | Two dimensional array | Multi-dimensional array(s) of values (zero dimensions to infinite dimensions) |

## How Vectors, Matrices, and Tensors Apply to an MLP
The reason modern neural nets use vectors, matrices, and tensors is to first have more complicated data/inputs. And also because using these data types allows for better leveraging of hardware that can do maths on these much faster than if they were individual scalars. 

But the mechanism of [[ML (Backpropogation)]] still apply to them, just on a mutli-dimensional level.

For example, we can use vectors and matrices to speed up operations, even if the input is a bunch of scalars.

But a bunch of scalars as input might be less efficient as they are scattered throughout memory, instead of a contiguous block which is nicer to work with. So, we might bunch them up into these vectors, matrices, and Tensors to also encode more complicated data at the same time. 

#ai #ai/conceptual  