# **[Day 14](./Day%2014): Dynamic Programming**

Welcome to Day 14 of **55 Days of DSA in Python**! Today, we dive into more dynamic programming problems, focusing on key sequence-based challenges: **Longest Increasing Subsequence (LIS)**, **Max Length of Pair Chain**, and **Russian Doll Envelopes**. These problems are crucial for solving optimization challenges involving sequences and subsequences, providing a strong foundation for working with DP techniques in various real-world applications.

---

### **Topics Covered:**
- Dynamic Programming  
- LIS  
- Max Length of Pair Chain  
- Russian Doll Envelopes  

---

### **1. Longest Increasing Subsequence (LIS)**
The Longest Increasing Subsequence (LIS) problem is about finding the longest subsequence in a sequence such that all the elements of the subsequence are sorted in increasing order.

#### **Approaches:**
There are multiple ways to solve this problem. We explore 5 different approaches, each with varying time complexities and space complexities:

##### **Approach 1: Recursion**
```python
def lengthOfLIS(nums):
    n = len(nums)
    def helper(curr, prev):
        if curr > n - 1:
            return 0
        exclude = helper(curr + 1, prev)
        include = 0
        if prev == -1 or nums[curr] > nums[prev]:
            include = 1 + helper(curr + 1, curr)
        return max(include, exclude)
    return helper(0, -1)
```
- **Time Complexity**: `O(2^n)` due to recursive calls.
- **Space Complexity**: `O(n)` for recursion stack.

##### **Approach 2: Memoization (Top-Down DP)**
```python
def lengthOfLIS(nums):
    n = len(nums)
    dp = [[-1] * n for _ in range(n)]
    def helper(curr, prev):
        if curr > n - 1:
            return 0
        if dp[curr][prev + 1] != -1:
            return dp[curr][prev + 1]
        exclude = helper(curr + 1, prev)
        include = 0
        if prev == -1 or nums[curr] > nums[prev]:
            include = 1 + helper(curr + 1, curr)
        dp[curr][prev + 1] = max(include, exclude)
        return dp[curr][prev + 1]
    return helper(0, -1)
```
- **Time Complexity**: `O(n^2)` due to the memoization table.
- **Space Complexity**: `O(n^2)` for the memoization table.

##### **Approach 3: Tabulation (Bottom-Up DP)**
```python
def lengthOfLIS(nums):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(i, -1, -1):
            exclude = dp[i + 1][j]
            include = 0
            if j - 1 == -1 or nums[i] > nums[j - 1]:
                include = 1 + dp[i + 1][i + 1]
            dp[i][j] = max(exclude, include)
    return dp[0][0]
```
- **Time Complexity**: `O(n^2)` due to the nested loops.
- **Space Complexity**: `O(n^2)` for the 2D DP table.

##### **Approach 4: Space Optimized DP (1D Array)**
```python
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    max_len = 1
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        if dp[i] > max_len:
            max_len = dp[i]
    return max_len
```
- **Time Complexity**: `O(n^2)` due to nested loops.
- **Space Complexity**: `O(n)` for the 1D DP array.

##### **Approach 5: Binary Search Approach (Efficient)**
```python
def lengthOfLIS(nums):
    def binarySearch(sub, num):
        left, right = 0, len(sub) - 1
        while left < right:
            mid = (left + right) // 2
            if sub[mid] < num:
                left = mid + 1
            else:
                right = mid
        return left
    
    sub = [nums[0]]
    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:
            index = binarySearch(sub, num)
            sub[index] = num
    return len(sub)
```
- **Time Complexity**: `O(n log n)` due to binary search.
- **Space Complexity**: `O(n)` for the subsequence list.

---

### **2. Max Length of Pair Chain**
The goal of the Max Length of Pair Chain problem is to find the longest chain of pairs where the second element of one pair is smaller than the first element of the next pair.

```python
def findLongestChain(pairs):
    n = len(pairs)
    pairs.sort()
    dp = [1] * n
    res = 1
    for i in range(1, n):
        for j in range(i):
            if pairs[j][1] < pairs[i][0] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        if dp[i] > res:
            res = dp[i]
    return res
```
- **Time Complexity**: `O(n^2)` due to nested loops.
- **Space Complexity**: `O(n)` for the DP array.

---

### **3. Russian Doll Envelopes**
This problem is about finding the maximum number of envelopes that can be nested (i.e., one envelope inside another). First, we sort the envelopes based on width and then use LIS to find the chain of heights.

```python
def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    n = len(envelopes)
    sub = [envelopes[0][1]]

    def binary_search(sub, num):
        left, right = 0, len(sub)
        while left < right:
            mid = (left + right) // 2
            if num > sub[mid]:
                left = mid + 1
            else:
                right = mid
        return left

    for i in range(1, n):
        num = envelopes[i][1]
        if num > sub[-1]:
            sub.append(num)
        else:
            x = binary_search(sub, num)
            sub[x] = num
    return len(sub)
```
- **Time Complexity**: `O(n log n)` due to sorting and binary search.
- **Space Complexity**: `O(n)` for the subsequence list.

---

## **Conclusion**

In **Day 14**, we covered key Dynamic Programming problems that involve sequences and subsequences, such as finding the longest increasing subsequence, the longest chain of pairs, and nested envelopes. Each approach offers a different perspective on solving these problems, with optimization strategies in terms of time and space complexity.

The solutions covered both bottom-up (tabulation) and top-down (memoization) dynamic programming approaches, along with binary search methods to optimize the LIS problem. These techniques are fundamental in solving a variety of problems efficiently using Dynamic Programming.