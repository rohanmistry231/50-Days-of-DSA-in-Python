# **Day 53: Graphs - Number of Connected Components & Topological Sort**

Welcome to **Day 53** of the **50 Days of DSA in Python**! In today’s session, we will delve into **graphs** and cover two important concepts:
- **Number of Connected Components**  
- **Topological Sort**  

Both of these concepts are essential in graph theory and have practical applications in many domains, from network analysis to project scheduling.

---

### **Topics Covered:**
- Number of Connected Components
- Topological Sort

---

## **1. Number of Connected Components**

### **Problem Statement**
In an undirected graph, a **connected component** is a set of nodes where there is a path between every pair of nodes in the component. The task is to count how many connected components exist in a given graph.

### **Approach**
- The problem can be solved using a Depth-First Search (DFS) or Breadth-First Search (BFS).
- Starting from an unvisited node, perform a DFS or BFS to mark all reachable nodes from that node.
- Each time we start a DFS/BFS from an unvisited node, it indicates a new connected component.

### **Steps**
1. Initialize a visited set to track visited nodes.
2. For each node, if it is unvisited, start a DFS/BFS to mark all reachable nodes.
3. Count the number of times you initiate a DFS/BFS, as this corresponds to the number of connected components.

### **Code (DFS Approach):**
```python
def count_connected_components(graph):
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    count = 0
    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1

    return count

# Example:
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3],
    5: []
}
print(count_connected_components(graph))  # Output: 3
```

### **Explanation:**
- We perform DFS starting from each unvisited node. Each DFS call explores all nodes in one connected component.
- The `count` variable keeps track of how many times a DFS is initiated, representing the number of connected components.

---

## **2. Topological Sort**

### **Problem Statement**
**Topological Sort** is the ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge from vertex `u` to vertex `v`, `u` comes before `v` in the ordering. Topological sorting is only possible if the graph has no cycles (i.e., it's a DAG).

### **Applications of Topological Sort:**
- Task scheduling (e.g., project management tools, job scheduling)
- Resolving dependencies (e.g., in package managers)

### **Approach**
Topological Sort can be done in two ways:
1. **DFS-based approach:** Perform a DFS and add nodes to the stack after all their descendants have been processed.
2. **Kahn’s Algorithm (BFS-based approach):** Use in-degree (number of incoming edges) and a queue to iteratively select nodes with zero in-degree and add them to the result.

### **Steps for DFS-based Approach:**
1. Perform a DFS traversal on the graph.
2. Mark each node as visited once it has been fully processed.
3. Add nodes to the result stack after all their neighbors are processed.
4. The stack will contain the topologically sorted nodes.

### **Code (DFS-based Topological Sort):**
```python
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)  # Add node to stack after processing all its neighbors

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Reverse the stack to get the correct order

# Example:
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
print(topological_sort(graph))  # Output: ['A', 'C', 'B', 'D']
```

### **Explanation:**
- The DFS approach explores all neighbors of a node before adding it to the stack, ensuring that all dependencies are processed first.
- The stack is reversed to give the correct topological order.

---

### **Code (Kahn’s Algorithm - BFS-based Topological Sort):**
```python
from collections import deque

def topological_sort_kahns(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    top_order = []

    while queue:
        node = queue.popleft()
        top_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(top_order) == len(graph):
        return top_order
    else:
        return []  # There is a cycle

# Example:
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
print(topological_sort_kahns(graph))  # Output: ['A', 'B', 'C', 'D']
```

### **Explanation:**
- Kahn’s algorithm iteratively adds nodes with zero in-degree to the queue, removes them from the graph, and updates the in-degrees of their neighbors.
- If all nodes are processed and added to the topological order, we have a valid topological sort. If not, the graph contains a cycle.

---

### **Conclusion**

In today’s session, we explored:
- **Number of Connected Components:** This is a basic graph traversal problem where we count how many isolated subgraphs exist in a graph.
- **Topological Sort:** This is a linear ordering of vertices in a directed acyclic graph (DAG). We covered both the DFS-based and Kahn’s Algorithm approaches for performing topological sorting.

These algorithms are essential for graph-related problems, particularly in project scheduling and dependency resolution.