### `&` Bitwise AND:
Compares each bit and returns `1` only if both values have `1` in the same position.
```c
A: 5 // decimal
   101 // binary

B: 4 // decimal
   100 // binary

A & B

	101
&   100
---------
	100 // Only gives you one when both binary numbers have 1 in the same position
```

So an use case will be: [[Fast Even or Odd Number Checker]]
### `^`  Bitwise XOR:
Exclusive OR: ≒ "difference detector", only returns `1` when the bits are different.
```c
0 ^ 0 = 0 // same, so returns 0
1 ^ 1 = 0 // same, so returns 0

1 ^ 0 = 1 // different, so returns 1
0 ^ 1 = 1 // different, so returns 1
```

```c
C: 3 // decimal
   011 // binary

D: 5 // decimal
   101 // binary

C ^ D

	011
^   101
---------
	110 // Only gives you 1 when both are different from each other
```

### `|` Bitwise OR:
Returns `1` if one of the bits is `1`
```c
E: 6 // decimal
   110 // binary

F: 2 // decimal
   010 // binary

E | F

	110
|   010
---------
	110 // Only returns 1 when either one is 1, because the last bit doesn't have 1 in either E or F, it is 0 
```

### `>>` & `<<` Bitwise Shift (Right and Left respectively):
#### `>>` Right Shift:
```c
9 >> 2

9 -> 0b1001 // binary

>> 2 // shift bits to the right by 2

0b10(01) // will be removed (right shift)

0b1001 >> 2 -> 0b10

0b10 -> 2 // decimal
```

#### `<<` Left Shift:
```c
10 << 2

10 -> 0b1010 // binary

<< 2 // shift bits to left by 2

0b1010(00) // 2 bits will be filled with zero, because of << "2"

0b1010 >> 2 -> 0b101000

0b101000 -> 40 // decimal
```

#C #C/features #explanation 