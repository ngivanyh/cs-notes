---
tags: [ai, ai/conceptual]
title: Neurons
date created: Monday, December 8th 2025, 6:26:04 pm
date modified: Sunday, May 3rd 2026, 10:00:18 pm
parent: Architectural and Conceptual
nav_order: 7
---
# Neurons
## Neurons — Knowhow
![[Neuron.png]]
Source: https://www.geeksforgeeks.org/machine-learning/activation-functions-neural-networks/

Looking at this diagram this "node" (neuron) receives three inputs: $x_1, x_2, x_3$ with weights $w_1, w_2, w_3$. These all funnel into the node which then calculates the *weighted sum* ($Z$) of all these inputs, i.e. $\sum_{i=1}^nw_i\cdot{x_i+b}$ with a added bias (in this case the upper limit $n$ is 3), which you could interpret as how sensitive it is to activation, if it isn't there the bias $b$ might be negative, for insensitive, and vice versa. 

Then the output $Z$ is passed into an activation function $f(Z)$, there are three popular [[Activation Functions|activation functions]]:
1. ReLU, defined as
$$max(0, Z)$$
2. $tanh(x)$, defined as
 $$\frac{e^{2x}-1}{e^{2x}+1}$$ 
3. $\sigma(x)$ (Sigmoid), defined as
$$\frac{1}{1+e^{-x}}$$

[This desmos graph can visualize them](https://www.desmos.com/calculator/hp93vmh41u).

#ai  #ai/conceptual 