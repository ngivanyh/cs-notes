---
tags: [ai, ai/conceptual]
title: MLPs (Feed-Forward Networks)
date created: Monday, December 8th 2025, 6:24:26 pm
date modified: Wednesday, March 11th 2026, 3:44:36 pm
parent: Architectural and Conceptual
grand_parent: AI
---
# MLPs (Feed-Forward Networks)
Short for **M**ulti **L**ayer **P**erceptrons. They are one of the simplest forms of neural networks. With multiple **layers** (which is basically a bunch of [[Neurons|neurons]]) that link together via weights and biases to output a result. 

![[MLP.webp]]
Source: https://oswalt.dev/2025/08/a-simple-neural-network-from-scratch/nn_scratch_topology_hu6702111761371884343.webp

As we can see in the picture, each "column" of neuron(s) is a layer, each layer can have a arbitrary amount of neurons. There are three different types of them, as noted by the picture:
- **Input Layer**: The values of the neurons in the input layer are simply the input values, so they are basically just registers that store the input data that will be passed onto the hidden layer.
- **Hidden Layer**: Where the magic happens, they shape the values passed in via their biases, weights, and activation functions.
- **Output Layer**: The layer where all the data gets funneled in and does a final calculation of $(\sum_{i=1}^{n}w_ix_i)+b$ and outputs them.

MLPs are in a lot of networks, they are perhaps the simplest neural network out there, the feed-forward layer in the modern [[Transformers and Modern LLMs|LLMs]] is also something resembling a MLP.

#ai #ai/conceptual  