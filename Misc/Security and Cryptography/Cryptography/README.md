---
date created: Sunday, April 5th 2026, 10:16:10 pm
date modified: Wednesday, July 29th 2026, 9:31:38 pm
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

 #cryptography #readme 
