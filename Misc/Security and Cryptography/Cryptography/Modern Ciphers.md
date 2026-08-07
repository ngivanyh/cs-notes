---
title: Modern Ciphers
date created: Friday, February 27th 2026, 6:01:24 pm
date modified: Friday, July 31st 2026, 11:08:12 am
---
# Modern Ciphers
Most modern cryptographic algorithms use keys $K$. Its the range of possible values is called the keyspace.

Algorithms that use keys put their keys as subscripts below the $E$ or $D$. If the keys are different for encryption and decryption, numbers would be put in subscript under the $K$.

## Symmetric Algorithms
Meaning algorithms whose ~~encryption and decryption keys are the same~~ encryption and decryption keys can be calculated from one another. Most of the time though, they are the same.

So, the key must remain a secret, hence its other names such as secret-key algorithms, etc. There are two categories within these algorithms; those who operate on the plaintext one bit/byte at a time (**stream ciphers/algorithms**), and those who operate on groups of bits called blocks at a time (**block ciphers/algorithms**)

## Public-Key Algorithms
Aka asymmetric algorithms, where the keys for encryption and decryption are different, and consequently cannot be derived from one another.

When we want to keep things secret:
- The key we encrypt the message is the public key, as the name suggests, it can be public
- The key we decrypt the message is the private/secret key, it is to be kept secret

However, in [[DSA|digital signatures]], we might reverse it, using the public key to decrypt and vice versa to verify authenticity.

#cryptography