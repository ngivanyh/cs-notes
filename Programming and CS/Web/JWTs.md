---
title: JWTs
date created: Friday, February 27th 2026, 8:37:29 pm
date modified: Thursday, July 30th 2026, 9:54:39 pm
---
# JWTs
## A JWT Dissected
**Full Spec: [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519)**

JWTs are often associated with security, when they are more like a session management scheme. They consist of a string (encoded w/ *base64URL*[^1]) separated by dots, the regex being:

```
(?P<Header>.+)\.(?P<Payload>.+)\.(?P<Signature>.+)
```

So, the first is the header, then it's the payload, and finally the signature. Now when we decode a JWT:

```json
{"alg":"HS256","typ":"JWT"}
{"exp":1786020320,"sub":"sub"} // placeholder sub value
SIGNATURE // placeholder signature
```

The header denotes the [[DSA|signing algorithm]] used and that this is an JWT.

The payload can contain many things, here it is the expiration of this token and the subject (the full list is defined in [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519)).

Finally is the signature, created by signing the header and payload with the private key/shared secret key (depending on the algorithm, because some don't generate public/private keys). [[Modern Ciphers#Public-Key Algorithms|Public-key algorithms]] can use their public key to validate the signature.

## JWTs in Action
When you login to an application, the app—if you've successfully authenticated—will give you a JWT that is authentic and signed by the application's private key.

Whatever subsequent requests the client makes to the application will include this JWT in the header of its requests, the server will verify the authenticity and give back the requested content.

`exp` is frequently set in JWTs, and both the client and the server can use it as a way to figure out if your session's expired, then promptly kick you out if you are.

## JWTs' Pitfalls
Since the token is in the client, it's hard to revoke the token; therefore, if attackers get ahold of a key that hasn't expired, they can run rampant throughout the system.

[^1]: Replaces the `+` and `/` characters used in base64 w/ `-` and `_` respectively

#web 