# **Day 54: Graphs - Number of Provinces & Find if Path Exists in Graph**

Welcome to **Day 54** of the **50 Days of DSA in Python**! Today, we will continue exploring **graphs** and focus on two interesting problems:
- **Number of Provinces**  
- **Find if Path Exists in Graph**  

Both of these problems involve graph traversal techniques and are essential for understanding real-world graph-related scenarios.

---

### **Topics Covered:**
- Number of Provinces
- Find if Path Exists in Graph

---

## **1. Number of Provinces**

### **Problem Statement**
In a graph where nodes represent cities and edges represent direct roads between cities, the number of **provinces** (also called **connected components**) refers to the number of groups of cities that are directly or indirectly connected by roads. The goal is to find how many provinces (connected components) exist in the graph.

### **Approach**
- The problem is equivalent to finding the number of connected components in an undirected graph.
- We can solve this using **DFS** or **BFS** to explore all the cities that are connected to each city and count how many times we start a new DFS/BFS.

### **Steps**
1. Iterate through each city.
2. If a city has not been visited, start a DFS or BFS from that city to mark all cities in its province as visited.
3. Each time we start a DFS/BFS from an unvisited city, it indicates a new province.

### **Code (DFS Approach):**
```python
def find_provinces(graph):
    visited = set()

    def dfs(city):
        visited.add(city)
        for neighbor in graph[city]:
            if neighbor not in visited:
                dfs(neighbor)

    count = 0
    for city in range(len(graph)):
        if city not in visited:
            dfs(city)
            count += 1

    return count

# Example:
graph = [
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 1, 1]
]
print(find_provinces(graph))  # Output: 2
```

### **Explanation:**
- The graph is represented as an adjacency matrix, where each element represents whether there is a direct road between two cities.
- We use DFS to explore all the cities in the same province and count how many DFS calls are made, which corresponds to the number of provinces.

---

## **2. Find if Path Exists in Graph**

### **Problem Statement**
Given a graph and two nodes, the task is to check if there is a path between the two nodes. The graph can be either directed or undirected.

### **Approach**
- This problem can be solved by performing a graph traversal (DFS or BFS) starting from one node and checking if we can reach the target node.
- We need to ensure that we do not visit the same node multiple times, which can be managed using a `visited` set.

### **Steps**
1. Start DFS/BFS from the source node.
2. If we reach the target node during traversal, return `True`.
3. If the traversal completes without reaching the target node, return `False`.

### **Code (DFS Approach):**
```python
def path_exists(graph, start, target):
    visited = set()

    def dfs(node):
        if node == target:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    return dfs(start)

# Example:
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: []
}
print(path_exists(graph, 0, 3))  # Output: True
print(path_exists(graph, 1, 3))  # Output: True
print(path_exists(graph, 0, 4))  # Output: False
```

### **Explanation:**
- The `dfs` function checks if there is a path from the starting node to the target node.
- We recursively explore all neighbors of the current node until we either find the target node or exhaust all possible paths.
- If we reach the target node, the function returns `True`, otherwise `False`.

---

### **Conclusion**

In today’s session, we learned about:
- **Number of Provinces:** This problem involves finding the number of connected components (provinces) in a graph using DFS.
- **Find if Path Exists in Graph:** This problem helps us determine if there is a path between two nodes in a graph using DFS.

These graph traversal techniques (DFS) are fundamental and will be useful in various applications, including network analysis, dependency resolution, and routing algorithms.