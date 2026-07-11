---
tags: [ai, ai/conceptual]
title: Neurons
date created: Monday, December 8th 2025, 6:26:04 pm
date modified: Saturday, July 11th 2026, 5:24:29 pm
parent: Architectural and Conceptual
nav_order: 9
---
# Neurons
![[Neuron.png]]
[Source](https://www.geeksforgeeks.org/machine-learning/activation-functions-neural-networks/)

Looking at this diagram this "node" (neuron) receives three inputs: $x_1, x_2, x_3$ with weights $w_1, w_2, w_3$. These all funnel into the node which then calculates the *weighted sum* ($Z$) of all these inputs, i.e. $(\sum_{i=1}^nw_i\cdot{x_i)+b}$ with a added bias (in this case the upper limit $n$ is 3), which you could interpret as how sensitive it is to activation, if it isn't there the bias $b$ might be negative, for insensitive, and vice versa. 

The value(s) of the neuron(s) at the end are called **logit(s)**, their output is most likely then placed through an activation function called **==Softmax==**. (See [[Activation Functions]] or [[MLPs (Feed-Forward Networks)]] for more about it)

Then the output $Z$ is passed into an activation function $f(Z)$, there are three iconic [[Activation Functions|activation functions]]:
1. ReLU, defined as
$$max(0, Z)$$
2. $tanh(x)$, defined as
 $$\frac{e^{2x}-1}{e^{2x}+1}$$ 
3. $\sigma(x)$ (Sigmoid), defined as
$$\frac{1}{1+e^{-x}}$$

[This desmos graph can visualize them](https://www.desmos.com/calculator/hp93vmh41u).

#ai  #ai/conceptual 