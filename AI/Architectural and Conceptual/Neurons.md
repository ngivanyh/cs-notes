---
tags: [ai, ai/conceptual]
title: Neurons
date created: Monday, December 8th 2025, 6:26:04 pm
date modified: Saturday, March 14th 2026, 10:02:23 pm
parent: Architectural and Conceptual
grand_parent: AI
---
# Neurons
## Neurons — Knowhow
![[Neuron.png]]
Source: https://www.geeksforgeeks.org/machine-learning/activation-functions-neural-networks/

Looking at this diagram this "node" (neuron) receives three inputs: $x_1, x_2, x_3$ with weights $w_1, w_2, w_3$. These all funnel into the node which then calculates the *weighted sum* ($Z$) of all these inputs, i.e. $\sum_{i=1}^nw_i\cdot{x_i+b}$ with a added bias (in this case the upper limit $n$ is 3), which you could interpret as how sensitive it is to activation, if it isn't there the bias $b$ might be negative, for insensitive, and vice versa. 

Then the output $Z$ is passed into an activation function $f(Z)$, there are three main activation functions:
1. ReLU, defined as
$$max(0, Z)$$
2. $tanh(x)$, defined as
 $$\frac{e^{2x}-1}{e^{2x}+1}$$ 
3. $\sigma(x)$ (Sigmoid), defined as
$$\frac{1}{1+e^{-x}}$$

[This desmos graph can visualize them](https://www.desmos.com/calculator/hp93vmh41u).
## Why Activation Functions?
If we visualize the whole neural network as a very big function $f(x,y,z,...)$, the introduction of activation functions inside each neuron can introduce non-linearity; aka, when you plot out $f(x,y,z,...)$ it isn't just a straight line, because the summation feeds its output into a non-linear function. Imagine it were just the summation passed onto the next neuron, then the multiple layers would be extra, since you can always simplify the expression into one big linear expression ($y=mx+b$). 

#ai  #ai/conceptual 