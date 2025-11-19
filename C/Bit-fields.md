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