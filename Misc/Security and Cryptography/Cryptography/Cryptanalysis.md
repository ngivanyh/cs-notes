---
title: Cryptanalysis
date created: Friday, July 31st 2026, 11:08:20 am
date modified: Tuesday, August 4th 2026, 6:14:26 pm
---
# Cryptanalysis
In laymen's terms: cracking the code; either getting the key or the plaintext.

A compromise is a loss of the key without going through cryptanalytic means, and an attempt in such means is called an attack.

## Attacks
Assumes the knowledge of the encryption algorithm used.

1. **Ciphertext-only attack**: Cryptanalyst has the ciphertext of several messages (encrypted using the same algorithm), they will try and get as many plaintexts of the messages as possible, or even try to deduce the key and decrypt all the messages that used that key.
2. **Known-plaintext attack**: Besides from having the ciphertext of many messages, they also possess the plaintext of those messages; they will try and deduce the key(s) used to encrypt the messages, and use the deduced keys to decrypt any new messages encrypted with the same key.
3. **Chosen-plaintext attack**: Known-plaintext attack but you can also **choose** what to encrypt, i.e. you have access to the encryption algorithm and you can test different plaintexts to deduce the key. Then of course, you can then decrypt new messages using the same key.
4. **Adaptive-chosen-plaintext attack**: In chosen-plaintext attacks, you only get to make the choices upfront, then encrypt them and gets the results and try to get the key; but *adaptive*-chosen-plaintext attacks allow you to have a feedback loop essentially, allowing you to adjust and get to the answer quicker (potentially).
5. **Chosen-ciphertext attack**: Opposite to the chosen-plaintext attack, you get the decryption function, ciphertexts, and the corresponding plaintexts, again your choices are made upfront. Primarily effective against asymmetric algorithms.
6. **Adaptive-chosen-ciphertext attack**: Number 5 but adaptive, akin to number 4.
7. **Chosen-key attack**: The cryptanalyst knows the relations between different keys
8. **Rubber-hose cryptanalysis**: Holding someone at gunpoint IRL until they give you the key. One of the methods—bribery—is also known as a **purchase-key attack**. 

To simplify:
1. Ciphertexts → Plaintexts (good)/Key(s) (better)
2. \[Ciphertexts ↔ Plaintexts\] → Key(s)
3. \[Choose plaintexts → Ciphertexts\] + \[Ciphertexts ↔ Plaintexts\] → Key(s)
4. 🔁\[Choose plaintexts → Ciphertexts\] + \[Ciphertexts ↔ Plaintexts\] → Key(s)
5. \[Choose ciphertexts → Plaintexts\] + \[Ciphertexts ↔ Plaintexts\] → Key(s)
6.  🔁\[Choose ciphertexts → Plaintexts\] + \[Ciphertexts ↔ Plaintexts\] → Key(s)
7. \[Key relationships\] + \[Plaintexts ↔ Ciphertexts\] → Key(s)
8. IRL (🔫/✉️/⚔/etc) → Key

#cryptography 