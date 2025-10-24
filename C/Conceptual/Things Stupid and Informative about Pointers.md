Pointers can do arithmetic, but say you have a `int a[3] = {1, 2, 3}`, then when you access the second element with `a[1]`, C will automatically convert that into `*(a+1)`. You might think that `+1` is just plus one like in maths, but in reality, since an `int` is four bytes, it really means "jump" by 1 `sizeof(int)`.

##### Stupid What Ifs:
- If `p` points to `0x10` and `q` points to `0x11`, `q - p < NULL` *might* result in `true`, but what we know is that the value would be useless as it'd point to a garbage location, and because pointers are unsigned, *maybe* it will overflow back and become `0xMAX - 0x-1`. (And it's also very stupid.
- Because in normal circumstances, `-1` on `type` pointer doesn't actually deduct one, if you were delusional, it wouldn't be easy to treat an (say) `int*` as a normal number.

#C #explanation