# **Day 13: Dynamic Programming - LCS and Edit Distance**

Welcome to Day 13 of **50 Days of DSA in Python**! Today, we explore two important problems in dynamic programming: **Longest Common Subsequence (LCS)** and **Edit Distance**. These problems are fundamental in string manipulation and pattern matching, and mastering them will provide a solid foundation for working with various algorithms in text processing and comparison.

---

### **Topics Covered:**
- Dynamic Programming
- Longest Common Subsequence (LCS)
- Edit Distance

---

## **1. Longest Common Subsequence (LCS)**

### **Problem Statement**
Given two strings, `text1` and `text2`, find the length of their **Longest Common Subsequence** (LCS). A subsequence is a sequence derived from another sequence by deleting some elements without changing the order of the remaining elements.

### **Approaches**

#### **1. Recursion (Brute Force Approach)**

The recursive approach involves checking all possible subsequences of both strings to find the longest common subsequence.

#### **Code:**
```python
def longestCommonSubsequence(text1, text2):
    """
    Calculate the length of the longest common subsequence using recursion.

    Args:
        text1 (str): The first input string.
        text2 (str): The second input string.

    Returns:
        int: The length of the longest common subsequence.
    """
    n = len(text1)
    m = len(text2)

    def helper(index1, index2):
        # Base case: If either index exceeds the length of the strings
        if index1 > n - 1 or index2 > m - 1:
            return 0

        # If characters match, include them in the subsequence
        if text1[index1] == text2[index2]:
            return 1 + helper(index1 + 1, index2 + 1)

        # Otherwise, consider both options (exclude current character of either string)
        return max(helper(index1 + 1, index2), helper(index1, index2 + 1))

    return helper(0, 0)
```

---

#### **2. Memoization (Top-Down Dynamic Programming)**

Memoization involves storing results of subproblems to avoid redundant calculations.

#### **Code:**
```python
def longestCommonSubsequence(text1, text2):
    """
    Calculate the length of the longest common subsequence using memoization.

    Args:
        text1 (str): The first input string.
        text2 (str): The second input string.

    Returns:
        int: The length of the longest common subsequence.
    """
    n = len(text1)
    m = len(text2)
    dp = [[-1] * m for _ in range(n)]

    def helper(index1, index2):
        # Base case: If either index exceeds the length of the strings
        if index1 > n - 1 or index2 > m - 1:
            return 0

        if dp[index1][index2] != -1:
            return dp[index1][index2]

        # If characters match, include them in the subsequence
        if text1[index1] == text2[index2]:
            dp[index1][index2] = 1 + helper(index1 + 1, index2 + 1)
            return dp[index1][index2]

        # Otherwise, consider both options (exclude current character of either string)
        dp[index1][index2] = max(helper(index1 + 1, index2), helper(index1, index2 + 1))
        return dp[index1][index2]

    return helper(0, 0)
```

---

#### **3. Tabulation (Bottom-Up Dynamic Programming)**

Tabulation involves solving the problem iteratively, filling a table with results of subproblems.

#### **Code:**
```python
def longestCommonSubsequence(text1, text2):
    """
    Calculate the length of the longest common subsequence using tabulation.

    Args:
        text1 (str): The first input string.
        text2 (str): The second input string.

    Returns:
        int: The length of the longest common subsequence.
    """
    n = len(text1)
    m = len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]
```

---

#### **4. Space Optimized Tabulation (Space Optimized Dynamic Programming)**

This approach optimizes the space complexity by using only two 1D arrays to store the previous and current rows of the DP table.

#### **Code:**
```python
def longestCommonSubsequence(text1, text2):
    """
    Calculate the length of the longest common subsequence using space optimized tabulation.

    Args:
        text1 (str): The first input string.
        text2 (str): The second input string.

    Returns:
        int: The length of the longest common subsequence.
    """
    n = len(text1)
    m = len(text2)
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr[:]

    return curr[m]
```

---

## **2. Edit Distance**

### **Problem Statement**
Given two words `word1` and `word2`, find the minimum number of operations required to convert `word1` into `word2`. The allowed operations are:
- Insert a character
- Delete a character
- Replace a character

### **Approaches**

#### **1. Recursion (Brute Force Approach)**

In this approach, we recursively compute the minimum number of operations by considering all possible operations.

#### **Code:**
```python
def minDistance(word1, word2):
    """
    Calculate the minimum edit distance between two words using recursion.

    Args:
        word1 (str): The first input word.
        word2 (str): The second input word.

    Returns:
        int: The minimum number of operations required to convert word1 to word2.
    """
    n = len(word1)
    m = len(word2)

    def number_of_operations(index1, index2):
        # Base case: If both indices exceed the length of the words
        if index1 > n - 1 and index2 > m - 1:
            return 0
        if index1 > n - 1:
            return m - index2
        if index2 > m - 1:
            return n - index1

        if word1[index1] == word2[index2]:
            return number_of_operations(index1 + 1, index2 + 1)

        insert = 1 + number_of_operations(index1, index2 + 1)
        delete = 1 + number_of_operations(index1 + 1, index2)
        replace = 1 + number_of_operations(index1 + 1, index2 + 1)

        return min(insert, delete, replace)

    return number_of_operations(0, 0)
```

---

#### **2. Memoization (Top-Down Dynamic Programming)**

Memoization stores the results of subproblems to avoid redundant calculations and speed up the solution.

#### **Code:**
```python
def minDistance(word1, word2):
    """
    Calculate the minimum edit distance between two words using memoization.

    Args:
        word1 (str): The first input word.
        word2 (str): The second input word.

    Returns:
        int: The minimum number of operations required to convert word1 to word2.
    """
    n = len(word1)
    m = len(word2)
    arr = [[-1] * m for _ in range(n)]

    def helper(index1, index2):
        # Base case: If indices exceed the length of the words
        if index1 < 0:
            return index2 + 1
        if index2 < 0:
            return index1 + 1

        if arr[index1][index2] != -1:
            return arr[index1][index2]

        if word1[index1] == word2[index2]:
            arr[index1][index2] = helper(index1 - 1, index2 - 1)
            return arr[index1][index2]

        replace = 1 + helper(index1 - 1, index2 - 1)
        delete = 1 + helper(index1 - 1, index2)
        insert = 1 + helper(index1, index2 - 1)

        arr[index1][index2] = min(replace, delete, insert)
        return arr[index1][index2]

    return helper(n - 1, m - 1)
```

---

####

 **3. Tabulation (Bottom-Up Dynamic Programming)**

Tabulation fills the DP table iteratively, considering all possible operations.

#### **Code:**
```python
def minDistance(word1, word2):
    """
    Calculate the minimum edit distance between two words using tabulation.

    Args:
        word1 (str): The first input word.
        word2 (str): The second input word.

    Returns:
        int: The minimum number of operations required to convert word1 to word2.
    """
    n = len(word1)
    m = len(word2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                replace = 1 + dp[i - 1][j - 1]
                delete = 1 + dp[i - 1][j]
                insert = 1 + dp[i][j - 1]
                dp[i][j] = min(delete, replace, insert)

    return dp[n][m]
```

---

#### **4. Space Optimized Tabulation (Space Optimized Dynamic Programming)**

In this approach, we use two 1D arrays to store the previous and current rows of the DP table.

#### **Code:**
```python
def minDistance(word1, word2):
    """
    Calculate the minimum edit distance between two words using space optimized tabulation.

    Args:
        word1 (str): The first input word.
        word2 (str): The second input word.

    Returns:
        int: The minimum number of operations required to convert word1 to word2.
    """
    n = len(word1)
    m = len(word2)

    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    for j in range(m + 1):
        prev[j] = j

    for i in range(1, n + 1):
        curr[0] = i
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                replace = 1 + prev[j - 1]
                delete = 1 + prev[j]
                insert = 1 + curr[j - 1]
                curr[j] = min(delete, replace, insert)
        prev = curr[:]

    return prev[m]
```

---

### **Conclusion**

Today we covered two essential string problems:
1. **Longest Common Subsequence (LCS)** with four approaches: Recursion, Memoization, Tabulation, and Space Optimized Tabulation.
2. **Edit Distance** with four approaches: Recursion, Memoization, Tabulation, and Space Optimized Tabulation.

By mastering these problems, you'll be better equipped to solve a wide range of string-related algorithmic challenges. Keep practicing, and see you tomorrow!