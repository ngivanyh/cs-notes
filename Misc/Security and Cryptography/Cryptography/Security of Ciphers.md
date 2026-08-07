---
title: Security of Ciphers
date created: Friday, July 31st 2026, 4:48:22 pm
date modified: Friday, July 31st 2026, 5:07:12 pm
---
# Security of Ciphers
## If...
- Cost to break > Value of encrypted data
- Time to break > Time of relevance for encrypted data
- Amount of data in 1 key < Amount of data needed to break
**==\=Safe==**[^1]

## Classification of Breaks
The severity of different types of algorithm breaks, as classified by Lars Knudsen:
1. **Total break**: The key is found, you're done for
2. **Global deduction**: The attacker finds an equivalent algorithm that circumvent needing knowledge of the key
3. **Instance (local) deduction**: The attackers gains plaintexts or ciphertexts not known previously
4. **Information deduction**: The attacker gains information about the key or plaintext
5. **Distinguishing algorithm**: The attacker can distinguish the cipher from a random one

## Security
**One time pads** are an **==unconditionally secure==** algorithm—*meaning no matter how much you know about the cipher, you can never get the plaintext*.

But cryptography mostly concerns itself with **==computationally secure==** algorithms, algorithms that are *practically* unbreakable. (I.E. you *could* brute force the keys given a ciphertext, but you wouldn't and probably shouldn't do so)

Complexities are written as orders of magnitude, so $2^{128}$ is a complexity, and it tells you that it takes 340282366920938463463374607431768211456 *operations* (long or short depending on what they are) to break the algorithm.

[^1]: *Probably*, who knows if your algorithm is suddenly worthless when you wake up one day

#cryptography 
