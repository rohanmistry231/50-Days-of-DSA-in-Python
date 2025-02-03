# **Day 15: Dynamic Programming**

Welcome to **Day 15** of **55 Days of DSA in Python**! Today, we dive into Dynamic Programming with a focus on solving problems related to **Palindromic Substrings**, **Longest Palindromic Substring**, and **Longest Palindromic Subsequence**. These problems are central in text processing and pattern recognition, and mastering them will strengthen your understanding of string manipulations and dynamic programming techniques.

---

## **Topics Covered:**
- Palindromic Substrings
- Longest Palindromic Substring
- Longest Palindromic Subsequence

---

### **1. Palindromic Substrings**
The Palindromic Substrings problem is about finding how many substrings in a given string are palindromes. A palindrome is a word or sequence that reads the same backward as forward.

#### **Approaches:**
We explore different approaches to solve the problem of counting palindromic substrings:

##### **Approach 1: Recursion with Memoization**
This approach uses a recursive function along with memoization to check if substrings are palindromes and count them.

```python
def countSubstrings(s):
    n = len(s)
    dp = [[-1] * n for _ in range(n)]

    def helper(i, j):
        if i == j:
            dp[i][j] = True
            return dp[i][j]
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        helper(i + 1, j)
        helper(i, j - 1)
        if s[i] == s[j] and (j == i + 1 or helper(i + 1, j - 1)):
            dp[i][j] = True
        else:
            dp[i][j] = False
        return dp[i][j]
    
    helper(0, n - 1)

    res = 0
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if dp[i][j] == True:
                res += 1
    return res
```
- **Time Complexity**: `O(n^2)` due to memoization.
- **Space Complexity**: `O(n^2)` for the DP table.

##### **Approach 2: Dynamic Programming (Bottom-Up)**
This approach uses a bottom-up DP table to find palindromic substrings by expanding from the center.

```python
def countSubstrings(s):
    res = 0
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if i == j:
                dp[i][j] = True
                res += 1
            elif s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1]):
                dp[i][j] = True
                res += 1
            else:
                dp[i][j] = False
    return res
```
- **Time Complexity**: `O(n^2)` due to nested loops.
- **Space Complexity**: `O(n^2)` for the DP table.

---

### **2. Longest Palindromic Substring**
The Longest Palindromic Substring problem involves finding the longest substring within a given string that is a palindrome.

#### **Approach:**
We use dynamic programming to build a DP table that stores whether substrings are palindromes and find the longest one.

```python
def longestPalindrome(s):
    n = len(s)
    dp = [[-1] * n for _ in range(n)]
    longest = ''

    for l in range(1, n + 1):
        for i in range(0, n - l + 1):
            j = i + l - 1
            if i == j:
                dp[i][j] = True
            elif s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1]):
                dp[i][j] = True
            else:
                dp[i][j] = False
            if dp[i][j]:
                longest = s[i:j + 1]
    return longest
```
- **Time Complexity**: `O(n^2)` due to nested loops.
- **Space Complexity**: `O(n^2)` for the DP table.

---

### **3. Longest Palindromic Subsequence**
The Longest Palindromic Subsequence problem is about finding the longest subsequence of a string that is a palindrome. Unlike substrings, the characters of subsequences are not required to be contiguous.

```python
def longestPalindromeSubseq(s):
    rev_s = s[::-1]
    n = len(s)

    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
        dp[0][i] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rev_s[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[n][n]
```
- **Time Complexity**: `O(n^2)` due to the nested loops.
- **Space Complexity**: `O(n^2)` for the DP table.

---

### **Conclusion**

Today, we explored three important problems related to palindromes in Dynamic Programming:

1. **Palindromic Substrings** with a focus on identifying all substrings that are palindromes.
2. **Longest Palindromic Substring** using dynamic programming to find the longest contiguous palindrome within a string.
3. **Longest Palindromic Subsequence**, where we tackled the problem of finding the longest subsequence (not necessarily contiguous) that is a palindrome.

Mastering these problems will enhance your ability to work with string manipulations and pattern recognition. Keep practicing to improve your skills in solving palindrome-based challenges. See you tomorrow for more exciting problems!