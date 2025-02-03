## Day 17: Word Break & Matrix Chain Multiplication

Welcome to Day 17 of **55 Days of DSA in Python**! Today, we explore two important problems in dynamic programming: **Word Break** and **Matrix Chain Multiplication**. These problems are crucial for understanding **string segmentation** and **optimal matrix multiplication**, both of which have wide applications in **text processing, compilation, and optimization problems**.

---

## **Problem 1: Word Break**

### **Problem Statement**
Given a string `s` and a dictionary `wordDict` containing a list of words, return `True` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

### **Approach 1: Normal DP (2D Table)**

```python
from typing import List

def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Determines if a string can be segmented into words from the dictionary using 2D DP.
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i:j + 1] in word_dict:
                dp[i][j] = True
            else:
                for k in range(i, j):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k + 1][j])
    
    return dp[0][n - 1]
```

### **Approach 2: Recursive Approach**

```python
from typing import List

def word_break_recursive(s: str, word_dict: List[str]) -> bool:
    """
    Determines if a string can be segmented into words from the dictionary using recursion.
    """
    def check_ending_at(index):
        if index < 0:
            return True
        for word in word_dict:
            if s[index - len(word) + 1:index + 1] == word and check_ending_at(index - len(word)):
                return True
        return False
    
    return check_ending_at(len(s) - 1)
```

### **Approach 3: Memoization (Top-Down DP)**

```python
from typing import List

def word_break_memoization(s: str, word_dict: List[str]) -> bool:
    """
    Determines if a string can be segmented into words from the dictionary using memoization.
    """
    n = len(s)
    dp = [-1] * n
    
    def check_build(i):
        if i < 0:
            return True
        if dp[i] != -1:
            return dp[i]
        for word in word_dict:
            if s[i - len(word) + 1:i + 1] == word and check_build(i - len(word)):
                dp[i] = True
                return dp[i]
        dp[i] = False
        return dp[i]
    
    return check_build(n - 1)
```

### **Approach 4: Tabulation (Bottom-Up DP)**

```python
from typing import List

def word_break_tabulation(s: str, word_dict: List[str]) -> bool:
    """
    Determines if a string can be segmented into words from the dictionary using tabulation.
    """
    n = len(s)
    dp = [False] * n
    
    for i in range(n):
        for word in word_dict:
            if i < len(word) - 1:
                continue
            if s[i - len(word) + 1:i + 1] == word and (i == len(word) - 1 or dp[i - len(word)]):
                dp[i] = True
                break
    
    return dp[n - 1]
```

---

## **Problem 2: Matrix Chain Multiplication**

### **Problem Statement**
Given an array `arr[]` of size `N` that represents the dimensions of matrices, determine the minimum number of scalar multiplications needed to compute the matrix chain product.

### **Approach 1: Recursive Approach**

```python
from typing import List

def matrix_multiplication_recursive(n: int, arr: List[int]) -> int:
    """
    Finds the minimum number of multiplications needed using recursion.
    """
    def find_cost(i, j):
        if i == j:
            return 0
        cost = float('inf')
        for k in range(i, j):
            curr_cost = find_cost(i, k) + find_cost(k + 1, j) + arr[i - 1] * arr[k] * arr[j]
            cost = min(cost, curr_cost)
        return cost
    
    return find_cost(1, n - 1)
```

### **Approach 2: Memoization (Top-Down DP)**

```python
from typing import List

def matrix_multiplication_memoization(n: int, arr: List[int]) -> int:
    """
    Finds the minimum number of multiplications needed using memoization.
    """
    dp = [[-1] * n for _ in range(n)]
    
    def find_cost(i, j):
        if i == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        cost = float('inf')
        for k in range(i, j):
            curr_cost = find_cost(i, k) + find_cost(k + 1, j) + arr[i - 1] * arr[k] * arr[j]
            cost = min(cost, curr_cost)
        dp[i][j] = cost
        return dp[i][j]
    
    return find_cost(1, n - 1)
```

### **Approach 3: Tabulation (Bottom-Up DP)**

```python
from typing import List

def matrix_multiplication_tabulation(n: int, arr: List[int]) -> int:
    """
    Finds the minimum number of multiplications needed using tabulation.
    """
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[1][n - 1]
```

---

## **Conclusion**

Today, we covered two essential problems in dynamic programming:
1. **Word Break** with four approaches: 2D DP, Recursion, Memoization, and Tabulation.
2. **Matrix Chain Multiplication** with three approaches: Recursion, Memoization, and Tabulation.

By mastering these problems, you'll strengthen your understanding of dynamic programming. Keep practicing, and see you tomorrow! 🚀