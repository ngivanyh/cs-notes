---
title: Graphs
date created: Sunday, August 9th 2026, 10:29:16 pm
date modified: Tuesday, October 27th 2026, 6:52:32 pm
---
# Graphs
Disambiguation:
- **Vertices** (Singular: Vertex): Nodes
- **Edge**: Connection
- **Digraph (Directed Graph)**: A graph where the the edge has a direction (basically)
- **Complete Graph**: A graph with $n$ nodes and $n\times (n-1)$ vertices
- **Strongly Connected**: Where two vertices ($u$, $v$) has an edge from $u$ to $v$ and vice versa
- **Indegree**: How many edges connect to a specific vertex (for digraphs)
- **Outdegree**: How many edges connect out to a vertex (for digraphs)
- **Cyclic/Acylic**: If the graph has any cycles ($u \leftrightarrow v$ (cyclic) or $u \rightarrow v$ (acyclic))

Trees, linked lists, and heaps are all a type of graph with extra restrictions. While [[MLPs (Feed-Forward Networks)|neural networks]] are digraphs with weights on the edges.

## Traversal
### Depth First Search (DFS)
DFS explores one adjacent vertex first, before going back to explore the other nodes, in a binary tree, it is akin to [[Trees#Pre-order|pre-order]] traversal.

DFS can be implemented in two ways, one is with recursion, the other iteration (with a loop) and a stack; both also need some way to mark the vertex as a visited one.

```python
def dfs(node):
    node.visited = True
    for n in node.adj:
        if not n.visited:
            dfs(n)

# or

dfs_stack = [source]
source.visited = True

while len(dfs_stack):
    node = dfs_stack.pop()
    for n in node.adj:
        if not n.visited:
            n.visited = True
            dfs_stack.append(n)
```

Properties of DFS:
- Finding reachability, cycles (not finding shortest path)
- Ancestry
- Reversing can create a topological sort of the graph[^1]
### Breadth First Search (BFS)
BFS finishes exploring all the adjacent vertices, before going one more level in the graph. In an unweighted graph, it can find the shortest path between two vertices. 

```python
from collections import deque as queue

bfs_queue = queue([source])
source.visited = True

while len(bfs_queue):
    node = bfs_queue.popleft()
    node.visited = True
    
    for n in node.adj:
        if not n.visited:
            n.visited = True
            bfs_queue.append(n)
```

Properties of BFS:
- Shortest path
- Detect cycles

[^1]: Is a kind of ordering within a directed, acyclic (no cycles) graph that for every vertex u to vertex v, always puts u before v. For a kind of directed acyclic graph, there may be multiple valid topological orders. 