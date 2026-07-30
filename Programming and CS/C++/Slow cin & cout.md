---
title: Slow cin
date created: Tuesday, July 14th 2026, 2:47:30 pm
date modified: Thursday, July 30th 2026, 8:09:19 am
---
# Slow `cin` & `cout`
`cin` and `cout` are notoriously slower than C's `scanf` and `printf`, that is because of these reasons:
- C++ streams are synchronized to the C streams, therefore C++ has this extra sync step to maintain its interoperability with C
- `cin` and `cout` streams are tied to each other

#cpp #cpp/conceptual
