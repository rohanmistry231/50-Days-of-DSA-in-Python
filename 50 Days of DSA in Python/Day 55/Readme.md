# **Day 55: Graphs - Number of Islands & Numbers with Same Consecutive Differences**

Welcome to **Day 55** of the **50 Days of DSA in Python**! Today, we will dive into **graph algorithms** and explore two intriguing problems:
- **Number of Islands**
- **Numbers with Same Consecutive Differences**

These problems highlight different ways of applying graph traversal techniques like **DFS** and **BFS** to solve grid-based problems.

---

### **Topics Covered:**
- Number of Islands
- Numbers with Same Consecutive Differences

---

## **1. Number of Islands**

### **Problem Statement**
Given a 2D grid map of `'1's` (land) and `'0's` (water), we need to find the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. The grid is rectangular and may have different dimensions.

### **Approach**
- This problem can be interpreted as a graph traversal problem where each `'1'` represents a land cell (node), and connections between adjacent land cells represent edges.
- We can perform a **Depth First Search (DFS)** or **Breadth First Search (BFS)** to explore all the land cells that are part of the same island and mark them as visited.
- Each DFS/BFS call that starts from an unvisited land cell corresponds to finding a new island.

### **Steps**
1. Iterate over each cell in the grid.
2. When encountering an unvisited land cell (`'1'`), perform a DFS/BFS to mark all connected land cells as visited.
3. Count the number of DFS/BFS calls made, as each corresponds to a new island.

### **Code (DFS Approach):**
```python
def num_islands(grid):
    if not grid:
        return 0

    def dfs(i, j):
        # Check boundaries and water
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        # Mark the land as visited
        grid[i][j] = '0'
        # Explore all 4 directions (up, down, left, right)
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':  # Found an unvisited land cell
                dfs(i, j)  # Perform DFS to mark all connected land cells
                count += 1  # Increment the island count

    return count

# Example:
grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
print(num_islands(grid))  # Output: 1
```

### **Explanation:**
- Each DFS call marks all land cells that belong to the current island, and we increment the island count each time we start a DFS from an unvisited land cell.

---

## **2. Numbers with Same Consecutive Differences**

### **Problem Statement**
Given two integers `n` and `k`, return all the numbers of length `n` such that the difference between every two consecutive digits is `k`. The solution should return the numbers in increasing order.

### **Approach**
- This problem involves generating numbers where the digits follow a specific consecutive difference rule.
- We can solve this using **backtracking** or **BFS**. We generate all valid numbers by adding digits that satisfy the consecutive difference condition.

### **Steps**
1. Start with each digit from 1 to 9 (since a number cannot start with 0).
2. For each starting digit, try adding the next digit that satisfies the consecutive difference condition.
3. Continue the process until the number has `n` digits.

### **Code (Backtracking Approach):**
```python
def nums_same_consec_diff(n, k):
    result = []

    def backtrack(num, length):
        if length == n:
            result.append(num)
            return

        last_digit = num % 10
        # Add the next possible digits based on the difference k
        if last_digit + k < 10:
            backtrack(num * 10 + last_digit + k, length + 1)
        if last_digit - k >= 0 and k != 0:
            backtrack(num * 10 + last_digit - k, length + 1)

    # Try starting from all digits from 1 to 9 (since the number cannot start with 0)
    for i in range(1, 10):
        backtrack(i, 1)

    return result

# Example:
print(nums_same_consec_diff(3, 7))  # Output: [181, 292, 707, 818, 929]
```

### **Explanation:**
- The backtracking function `backtrack` generates valid numbers by checking if the last digit plus or minus the consecutive difference `k` results in a valid next digit (between 0 and 9).
- This process continues until the number has `n` digits.

---

### **Conclusion**

In today’s session, we explored two important problems involving **graphs** and **number generation**:
- **Number of Islands:** We learned how to find the number of connected components (islands) in a 2D grid using DFS.
- **Numbers with Same Consecutive Differences:** We used backtracking to generate numbers of length `n` where consecutive digits have a specified difference `k`.

Both problems involve important algorithmic techniques and can be applied to real-world problems such as connectivity in grids or digit-based number generation.