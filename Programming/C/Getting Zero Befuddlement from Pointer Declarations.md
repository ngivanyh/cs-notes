---
title: Getting Zero Befuddlement from Pointer Declarations
date created: Wednesday, April 8th 2026, 4:03:21 pm
date modified: Saturday, April 11th 2026, 9:50:50 pm
tags: [C, programming]
parent: C
nav_order: 6
---
# Getting Zero Befuddlement from Pointer Declarations
## Setting the Better Naming Scheme
The most confusion-free way to declare pointers is to separate spaces for every element in the declaration, including the `*`. Examples:

- `const * double a`
- `unsigned long long * const b`
- `int * c`
- `static double * a`

## Reading from Right to Left
Now that we've separated these things, reading them from right to left makes everything clear as day. Before, things like `const double * a` and `double * const a` seem very much like the same, but reading from right to left will differentiate them:

`const double * a` is a pointer `a` that points to a `const double`
`double * const a` is a `const` pointer `a` that points to a `double`

#C #programming 