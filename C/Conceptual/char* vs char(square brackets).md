`char*` and `char[]` are very similar, they are both pointers to a char array. BUT `char*` is unmodifiable, the value the pointer points to is stored in read-only memory, whilst `char[]` can be modified with syntax like this: `char a[2] = "hi"; a[1] = 'e'`

#C #C/conceptual #explanation 