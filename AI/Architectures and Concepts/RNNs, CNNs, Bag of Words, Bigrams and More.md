---
title: RNNs, CNNs, Bag of Words, Bigrams and More
date created: Tuesday, January 27th 2026, 10:43:20 pm
date modified: Tuesday, October 27th 2026, 6:37:38 pm
---
# RNNs, CNNs, Bag of Words, Bigrams and More
## RNNs

## CNNs

## Bag of Words

## n-grams
n-gram models analyze data in chunks of n units. For bigram character model, it will analyze two characters at a time.

Based on how many chunks appear, you can create a probability distribution the model can use to make its choice. For example, in a bigram character model:

```
ia: 30%
ib: 10%
ic: 30%
id: 20%
ie: 10%
```

Then the model is more likely to output either `ia` or `ic`, because they had more occurrences within the training data.

For n-grams, each character or digit or whatever unit you use is one token.
## Diffusion Models

## [[Transformers and Modern LLMs|Transformers]]

#ai #ai/conceptual  