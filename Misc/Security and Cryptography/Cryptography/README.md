---
date created: Sunday, April 5th 2026, 10:16:10 pm
date modified: Friday, July 31st 2026, 4:47:57 pm
title: README
---
# README
Knowledge about cryptography, substantial parts scoured from *Applied Cryptography*.

## Fundamentals
A person is sending plaintext $M$/$P$ to another person, and $M$ (for message) is something to encrypt (or "encipher" in ISO 7498-2) into ciphertext $C$, the receiver then decrypts (deciphers) this $C$ back to $M$. $M$ becomes $C$ through an encryption function $E$, forming the relation:

$$E(M)=C$$

The reverse process, decryption, passes through the decryption function $D$, therefore:

$$D(C)=M$$

The whole point of this is to first encrypt the message so it doesn't get understood by parties you don't give access to and then decrypt it once it's in the right hands, so this must be true:

$$D(E(M))=M$$

Sending messages is one use, other uses include:
- Authentication (aka "auth")
- Validating Integrity (of the message)
- Nonrepudiation (the sender cannot deny their sending of a message)

The mathematical function used for encryption and decryption is called a cryptographic algorithm (cipher), a *restricted* one means the inner working of the algorithm are not revealed. But the best ciphers are the ones whose inner workings have been made public, yet still keep your thing secure.

**Disambiguation:** *Encoding* and *encryption* are two different things, the former means to turn one format into another, e.g. Big5 to UTF-8 needs an *encoding* process; whilst encryption might need a key, and is meant to have security implications, the former doesn't need to have so.

 #cryptography #readme 
