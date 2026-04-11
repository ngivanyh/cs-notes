---
tags: [ai, ai/conceptual]
title: Transformers and Modern LLMs
date created: Saturday, September 6th 2025, 3:14:26 pm
date modified: Saturday, April 11th 2026, 9:52:49 pm
parent: Architectural and Conceptual
nav_order: 11
---
# Transformers and Modern LLMs
**Attention Is All You Need [Paper](https://arxiv.org/pdf/1706.03762)**
**[3 Blue 1 Brown video](https://youtu.be/wjZofJX0v4M)**

## The Core Innovation: Attention
**Attention**, is the core of a transformer, which is an improvement to RNNs (basically [[MLPs (Feed-Forward Networks)|MLPs]] that run multiple times by itself).

## How Modern LLMs Work
Some nouns:
- Temperature: How random the model takes the probability distribution of next tokens. Higher is more creative and sporadic, 0 is very grounded and logical.
- Top-k: The number of samples to sample from in the probability distribution of next tokens.
- Top-p: The minimum percentage probability to take from the distribution, do not set top-k if this is set to another a value.

#ai #ai/conceptual  