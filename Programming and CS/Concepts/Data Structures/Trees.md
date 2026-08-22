---
title: Trees
date created: Tuesday, July 14th 2026, 3:11:31 pm
date modified: Monday, August 10th 2026, 10:05:31 am
---
# Trees
![[Tree.png]]
[Source](https://cs.stackexchange.com/questions/153714/algorithm-to-recreate-a-splay-tree)

Disambiguation:
- **Leaf Nodes**: Terminal Nodes
- **Edges**: Connections
- **Full Binary Tree**: Binary trees where each node has either 0 or 2 children
- **Pathological/Degenerate Binary Trees**: ~~Binary trees~~ Essentially a linked list (each node has one child)
- **Complete Binary Tree**: Binary trees where all levels are filled, and all left nodes lean to the left
- **Perfect Binary Tree**: Binary trees where all nodes have 2 children (except leaf nodes)
- **Balanced Binary Tree**: Binary trees where the left and right subtrees differ in height by no more than 1 (height is $O(\log n)$)

## Waste
For an **$n$-ary tree stored as a linked list** (the other method is in the binary tree code below) with $m$ nodes, you must allocate $n\times m$ pointers to your children into the linked list. This tree, which has $m-1$nodes, means you waste $n\times m-(m-1)$ linked list slots.

| $n$ | Waste                |
| --- | -------------------- |
| 2   | $\approx\frac{1}{2}$ |
| $3$ | $\approx\frac{2}{3}$ |
| $4$ | $\approx\frac{3}{4}$ |

```
Example:

  A
 / \
B   C

n = 2
m = 3

Allocated: 2 * 3 = 6
Used: Pointer to B, Pointer to C
```

So the waste equation ($W$) is:

$$
W=\frac{n\times m-(m-1)}{n\times m}
$$

## Binary Trees
Evidently from the table above, binary trees are the most efficient and most common type of tree. And they are the only type of tree that can represent an empty set ($\phi$).

```python
"""
Binary Tree using a Regular List

Allocates a perfect binary tree
(i.e. all nodes have 0/2 children)
"""

Tree = [1, 2, 3, 7, None, 9, 10]

def index(expr: str):
    """
    the tree traverse expr starts from the head node
    
    L/l for left of the node
    R/r for the right
    """
    
    end_idx = 1
    expr = expr.lower()
    for command in expr:
        end_idx = 2*end_idx if command == "l" else 2*end_idx + 1
    return Tree[end_idx - 1]

print(index("lr")) # prints None
```

The above uses a regular `list` (array) to store the whole tree, in languages with OOP though:

```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

Binary search trees are binary trees but the child node is a node whose value is less than or equal to the parent, and vice versa for the right

### Traversal
Using the node definition up top (passing the `n` as `0` (the top node)), and this tree:

![[Tree Traversal Example.png]]
Created using [this web app](https://tree-visualizer.netlify.app/)
#### Pre-order
1. Visit parent nodes
2. Visit left nodes
3. Visit right nodes

```python
def preorder(n):
    if n.value is not None:
        print(f"{n.value} ")
        preorder(n.left)
        preorder(n.right)
```

Result: `0 1 3 5 6 7 8 4 2`
#### In-order
1. Visit left nodes
2. Visit parent nodes
3. Visit right nodes

```python
def inorder(n)
    if n.value is not None:
        inorder(n.left)
        print(f"{n.value} ")
        inorder(n.right)
```

Result: `5 3 7 6 8 1 4 0 2 `
#### Post-order
1. Visit left nodes
2. Visit right ondes
3. Visit parent nodes

```python
def postorder(n):
    if n.value is not None:
        postorder(n.left)
        postorder(n.right)
        print(f"{n.value} ")
```

Result: `5 7 8 6 3 4 1 2 0 `

#data-structures 