---
title: Cycle
date created: Tuesday, January 20th 2026, 4:45:03 pm
date modified: Friday, August 7th 2026, 11:06:10 am
---
# Cycle
*Not necessarily a data structure, but it is kind of like one*

Cycles through items in a list, rolls over.

## Using Indices

```python
l = [1, 2, 3, ...]

# access next item
l[(current_index + 1) % len(l)]

# access previous item
l[(current_index - 1 + len(l)) % len(l)]
```

The `%` (modulo) operator is not just useful for checking if a number is a multiple of something, it's also useful for cycling/repeating things.

## Circular Linked Lists

```c
#include <stdlib.h>

typedef struct LinkedList {
    int value;
    struct LinkedList * next;
} LinkedList;

void Add(LinkedList * list, int value)
{
    if (list == NULL)
        return;
    
    LinkedList * new = (LinkedList *) malloc(sizeof(LinkedList));
    new->value = value;
    
    for (LinkedList * l = list; l->next != list; l = l->next)
        ;
        
    l->next = new;
    new->next = list; // would be NULL in a singly-linked list
}
```

#programming #data-structures 