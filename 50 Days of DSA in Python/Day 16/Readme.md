# **Day 16: Dynamic Programming**

Welcome to Day 16 of **50 Days of DSA in Python**! Today, we focus on two important problems in **Dynamic Programming**: **Palindrome Partitioning** and **Palindrome Partitioning 2**. These problems are essential in understanding **string manipulation** and **optimal partitioning strategies**, particularly when working with palindromes.

---

## **Topics Covered:**
- Dynamic Programming
- Palindrome Partitioning
- Palindrome Partitioning 2

---

## **1. Palindrome Partitioning**

The **Palindrome Partitioning** problem is about partitioning a given string into **substrings** such that each substring is a **palindrome**. The goal is to generate all possible valid partitions.

### **Approach: Backtracking with Precomputed Palindromes**
We use **backtracking** to explore all possible partitions while **precomputing** palindrome checks using a **DP table**.

```python
def partition(s):
    """
    Generates all possible palindrome partitions of a given string.

    Args:
        s (str): The input string.

    Returns:
        List[List[str]]: A list of all possible palindrome partitions.
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j:
                dp[i][j] = True
            elif s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1]):
                dp[i][j] = True
    
    def helper(index, curr_partition):
        if index >= n:
            result.append(curr_partition[:])
            return
        for i in range(index, n):
            if dp[index][i]:
                curr_partition.append(s[index:i + 1])
                helper(i + 1, curr_partition)
                curr_partition.pop()
    
    result = []
    helper(0, [])
    return result
```
- **Time Complexity**: `O(2^n * n)` (Exponential due to backtracking)
- **Space Complexity**: `O(n^2)` (for DP table)

---

## **2. Palindrome Partitioning 2**
The **Palindrome Partitioning 2** problem is about **finding the minimum number of cuts** needed to partition a string such that every substring is a **palindrome**.

### **Approaches:**
We explore **four** different approaches to solve this problem efficiently.

#### **Approach 1: Backtracking (Brute Force)**
```python
def min_cut(s):
    """Backtracking approach without dynamic programming."""
    def is_palindrome(start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def partitions(start, end):
        if start == end or is_palindrome(start, end):
            return 0
        min_cuts = end - start
        for end_index in range(start, end):
            if is_palindrome(start, end_index):
                min_cuts = min(min_cuts, 1 + partitions(end_index + 1, end))
        return min_cuts
    
    return partitions(0, len(s) - 1)
```
- **Time Complexity**: `O(2^n * n)`
- **Space Complexity**: `O(n)`

#### **Approach 2: Memoization (Top-Down DP)**
```python
def min_cut(s):
    """Top-down DP with memoization."""
    n = len(s)
    is_palindrome = [[None] * n for _ in range(n)]
    min_cuts = [[None] * n for _ in range(n)]
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j:
                is_palindrome[i][j] = True
            elif s[i] == s[j] and (j == i + 1 or is_palindrome[i + 1][j - 1]):
                is_palindrome[i][j] = True
            else:
                is_palindrome[i][j] = False
    
    def partitions(start, end):
        if start == end or is_palindrome[start][end]:
            return 0
        if min_cuts[start][end] is not None:
            return min_cuts[start][end]
        min_cuts[start][end] = end - start
        for end_index in range(start, end):
            if is_palindrome[start][end_index]:
                min_cuts[start][end] = min(min_cuts[start][end],
                                           1 + partitions(end_index + 1, end))
        return min_cuts[start][end]
    
    return partitions(0, len(s) - 1)
```
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)`

#### **Approach 3: Tabulation (Bottom-Up DP - Approach A)**
```python
def min_cut(s):
    """Bottom-up DP using a 2D table."""
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j or (s[i] == s[j] and dp[i + 1][j - 1] == 0):
                dp[i][j] = 0
            else:
                dp[i][j] = j - i
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], 1 + dp[i][k] + dp[k + 1][j])
    
    return dp[0][n - 1]
```
- **Time Complexity**: `O(n^3)`
- **Space Complexity**: `O(n^2)`

#### **Approach 4: Tabulation (Bottom-Up DP - Approach B)**
```python
def min_cut(s):
    """Optimized Bottom-up DP using a 1D DP array."""
    n = len(s)
    is_palindrome = [[False] * n for _ in range(n)]
    dp = [0] * n
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j or (s[i] == s[j] and (j == i + 1 or is_palindrome[i + 1][j - 1])):
                is_palindrome[i][j] = True
    
    for end in range(n):
        min_cuts = end
        for start in range(end + 1):
            if is_palindrome[start][end]:
                min_cuts = 0 if start == 0 else min(min_cuts, 1 + dp[start - 1])
        dp[end] = min_cuts
    
    return dp[n - 1]
```
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)`

---

## **Conclusion**

Today, we explored **Palindrome Partitioning** and **Palindrome Partitioning 2**, covering **Backtracking**, **Memoization**, and **Tabulation** techniques. Mastering these approaches will help in solving many **string-based** problems efficiently. Keep practicing, and see you tomorrow! 🚀