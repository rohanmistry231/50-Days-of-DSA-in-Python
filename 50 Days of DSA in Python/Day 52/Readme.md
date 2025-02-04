# **Day 52: Graphs - BFS & DFS**

Welcome to **Day 52** of the **50 Days of DSA in Python**! Today, we dive into **Graphs** and explore two essential graph traversal algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. These algorithms are foundational for solving problems involving graphs and are widely used in pathfinding, search problems, and more.

---

### **Topics Covered:**
- BFS (Breadth-First Search)
- DFS (Depth-First Search)

---

## **1. BFS (Breadth-First Search)**

### **Problem Statement**  
**Breadth-First Search (BFS)** is a graph traversal algorithm that starts from a source node and explores all the neighboring nodes at the present depth before moving on to nodes at the next depth level. BFS is typically used for finding the shortest path in unweighted graphs.

### **Properties of BFS:**
- Explores the graph level by level.
- Uses a queue data structure to manage the nodes to be explored.
- Ensures the shortest path in an unweighted graph.
- Useful in algorithms like finding the shortest path and connected components.

### **Approach to BFS:**
1. Start from the source node.
2. Mark the source node as visited and enqueue it.
3. While the queue is not empty, dequeue a node and visit all its unvisited neighbors, marking them as visited and enqueueing them.
4. Repeat until all reachable nodes have been visited.

### **Code:**
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")  # Visit the node (you can process it here)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example:
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}
bfs(graph, 0)  # Output: 0 1 2 3 4
```

### **Explanation:**
- **Queue:** A queue is used to explore nodes in the order they are discovered.
- **Visited Set:** A set is used to keep track of the visited nodes to avoid revisiting them.

---

## **2. DFS (Depth-First Search)**

### **Problem Statement**  
**Depth-First Search (DFS)** is a graph traversal algorithm that starts from a source node and explores as far as possible along each branch before backtracking. DFS is particularly useful for problems like finding connected components, cycle detection, and topological sorting.

### **Properties of DFS:**
- Explores the graph by going as deep as possible before backtracking.
- Can be implemented using either recursion or an explicit stack.
- Useful for pathfinding, connected components, and tree traversal.

### **Approach to DFS:**
1. Start from the source node.
2. Mark the node as visited.
3. Explore all the unvisited neighbors of the node recursively (or using a stack).
4. Repeat until all reachable nodes are visited.

### **Code (Recursive DFS):**
```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=" ")  # Visit the node (you can process it here)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example:
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}
dfs(graph, 0)  # Output: 0 1 3 4 2
```

### **Code (Iterative DFS using Stack):**
```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")  # Visit the node (you can process it here)

            for neighbor in reversed(graph[node]):  # Reversed to maintain order of exploration
                if neighbor not in visited:
                    stack.append(neighbor)

# Example:
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}
dfs_iterative(graph, 0)  # Output: 0 2 1 4 3
```

### **Explanation:**
- **Recursive DFS:** The function calls itself for each unvisited neighbor, diving as deep as possible.
- **Iterative DFS:** A stack is used instead of recursion, allowing the algorithm to explore nodes iteratively.

---

### **Comparison Between BFS and DFS:**
| **Characteristic**         | **BFS**                            | **DFS**                            |
|----------------------------|------------------------------------|------------------------------------|
| **Traversal Strategy**      | Level by level (breadth-first)     | Deep as possible, then backtrack   |
| **Data Structure Used**     | Queue                              | Stack (or recursion)               |
| **Space Complexity**        | O(V) (for visited nodes)           | O(V) (for recursion or stack)     |
| **Shortest Path**           | Finds shortest path in unweighted graphs | Does not guarantee shortest path   |
| **Applications**            | Shortest path, level-order traversal | Pathfinding, cycle detection, topological sorting |

---

### **Conclusion**

In today's session, we covered two fundamental graph traversal techniques:
- **BFS (Breadth-First Search):** Traverses the graph level by level using a queue. It's particularly useful for finding the shortest path in unweighted graphs.
- **DFS (Depth-First Search):** Explores the graph deeply, using either recursion or a stack. It is useful for tasks like cycle detection, pathfinding, and topological sorting.

Both BFS and DFS are core algorithms in graph theory and have a variety of applications in solving real-world problems.