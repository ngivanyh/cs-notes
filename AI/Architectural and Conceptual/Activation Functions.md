---
tags: [ai, ai/conceptual]
title: Activation Functions
date created: Wednesday, January 28th 2026, 8:15:02 am
date modified: Saturday, July 11th 2026, 5:21:46 pm
parent: Architectural and Conceptual
nav_order: 1
---
# Activation Functions
## Why Activation Functions?
If we visualize the whole neural network as a very big function $f(x,y,z,...)$, the introduction of activation functions inside each neuron can introduce non-linearity; aka, when you plot out $f(x,y,z,...)$ it isn't just a straight line, because the summation feeds its output into a non-linear function. Imagine it were just the summation passed onto the next neuron, then the multiple layers would be extra, since you can always simplify the expression into one big linear expression ($y=mx+b$).

Non-linear functions allow the model to understand more complex patterns, it doesn't mean linear functions aren't useful, they just cannot create models that do tasks as complex as modern neural networks.

## Vanishing and Exploding Gradients
- **Vanishing Gradients**: Gradients become very small, almost 0; causes weight/bias updates to be minute
- **Exploding Gradients**: Gradients become very large, weight/bias updates will drastically change model output

## Different Activation Functions
| Function                                     | Definition                              | Derivative                                        | Upsides                                                     | Downsides                                                                      |
| -------------------------------------------- | --------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Linear                                       | $f(x)=x$                                | 1                                                 | Efficient                                                   | Linearity limits the model's ability to learn complex patterns                 |
| ReLU                                         | $ReLU(x)=max(x, 0)$                     | If $f(x)=0$, $f'(x)=0$; else $f'(x)=1$ ($f(x)=x$) | Efficient, doesn't vanish gradients                         | Since negative weighted sums are just 0, it causes parts of the model to "die" |
| $\tanh{x}$                                   | $\tanh x=\frac{e^x-e^{-x}}{e^x+e^{-x}}$ | $1-tanh^2x$                                       | Symmetrical on $(0, 0)$, steeper gradient than Sigmoid      | Costly to compute, vanishing gradients                                         |
| Sigmoid ($\sigma()$)                         | $\sigma(x)=\frac{1}{1+e^{-x}}$          | $\sigma(x)(1-\sigma(x))$                          | Squashes inputs to somewhere between 0 and 1                | Not centered at $(0, 0)$, vanishing gradients, costly to compute               |
| [GELU](https://arxiv.org/pdf/1606.08415)[^1] | $GELU(x)=x\cdot P(X\le x)$              | Input($x$)-dependent                              | Doesn't completely kill potentially helpful negative values | More expensive than ReLU                                                       |
| Softmax                                      |                                         |                                                   |                                                             |                                                                                |
| And More                                     | Function-dependent                      | Function-dependent                                | Improves on mostly ReLU                                     | May be more expensive than ReLU                                                |

## Why these Activation Functions?

[^1]: GeLU is an improvement to ReLU, the link is hyperlinked onto the "GeLU" text, full URL: https://arxiv.org/pdf/1606.08415. The cool thing about GeLU (and some other activation functions) is that it's not a hard mapping of $x$ to an output, i.e. the function behaves differently depending of the input. It is taking over because it isn't as blunt as ReLU, which will squash all the negatives, making the model able to factor in these negative computations, with the negatives being *larger* (because the number behind the - sign is smaller). GELU can be approximated with $0.5x(1+tanh[\sqrt{\frac{2}{\pi}}(x+0.044715x^3 )])$.[^2]
[^2]: $x$ means the single weighted sum (+ the bias) of the neuron, or if we're dealing with vectors and other things, 

#ai #ai/conceptual 