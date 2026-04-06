---
tags: [C, C/features]
title: Bit-fields
date created: Thursday, October 30th 2025, 6:17:47 am
date modified: Monday, April 6th 2026, 8:28:46 am
parent: C
nav_order: 1
---
# Bit-fields
“Field” for short, used when storage space is at a premium, kinda like IDs.

```c

struct {
    unsigned int a: 1;
    unsigned int b: 1;
    unsigned int c: 1;
} fields;

```

The `: 1` means a one bit field. Almost everything about fields are implementation-dependent. Fields are not so great (not very portable, specify `signed` for `unsigned` for portability) some are left to right, some are right to left (defined from). Fields must only be `int`s.

**Features of bit-fields**:
- Unnamed, with a number behind: Basically just making a padding of N bits, reserving that space for nothing, just for purposes of alignment.
- Unnamed, width of 0: specifying a boundary between different bit-fields.

The reason it can be used for alignment is because operating systems like reading memory in chunks, instead of a small unit like 1 byte. Say your OS reads in 4 byte chunks at a time, then even though a `char` would only fill in one of those 4 bytes, the OS will pad that 4 byte chunk to 4 bytes.

#C #C/features 