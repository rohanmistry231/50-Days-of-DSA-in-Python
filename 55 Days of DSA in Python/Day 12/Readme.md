# **Day 12: Dynamic Programming - Target Sum and Partition Equal Subset Sum**

Welcome to Day 12 of **55 Days of DSA in Python**! Today, we continue our journey in **Dynamic Programming** by exploring two important problems: **Target Sum** and **Partition Equal Subset Sum**. These problems will help us deepen our understanding of **subset sum variation** and **state transitions** in DP.

---

### **Topics Covered:**
- Dynamic Programming
- Target Sum
- Partition Equal Subset Sum

---

## **1. Dynamic Programming Overview**

Dynamic Programming (DP) is an optimization technique used to solve problems by breaking them down into smaller subproblems and storing their results to avoid redundant computations.

### **Key Concepts**
- **Overlapping Subproblems**: Problems that can be broken down into smaller problems that are solved multiple times.
- **Optimal Substructure**: The optimal solution can be built from optimal solutions of subproblems.
- **Memoization (Top-Down)**: Storing already computed results to avoid recalculating.
- **Tabulation (Bottom-Up)**: Building the solution iteratively using an array or matrix.

---

## **2. Target Sum**

### **Problem Statement**
Given an array `nums` of integers and an integer `target`, you need to assign `+` or `-` to each element in `nums` such that the sum of the resulting numbers equals `target`. Return the number of ways to achieve this target sum.

### **Approach**
We can solve this problem using **Dynamic Programming** by recognizing it as a variation of the **subset sum** problem.

### **Optimized DP Solution**

```python
from typing import List

def find_target_sum_ways(nums: List[int], target: int) -> int:
    """
    Find the number of ways to assign symbols '+' and '-' to make the sum equal to the target.

    Args:
        nums (List[int]): List of numbers.
        target (int): Target sum to achieve.

    Returns:
        int: Number of ways to reach the target sum.
    """
    n = len(nums)
    summation = sum(nums)
    dp = [[None] * (2 * summation + 1) for _ in range(n)]

    def helper(index: int, sum_nums: int) -> int:
        if index < 0:
            return 1 if sum_nums == target else 0
        if dp[index][sum_nums + summation] is not None:
            return dp[index][sum_nums + summation]

        negative = helper(index - 1, sum_nums - nums[index])
        positive = helper(index - 1, sum_nums + nums[index])
        dp[index][sum_nums + summation] = negative + positive
        return dp[index][sum_nums + summation]
    
    return helper(n - 1, 0)
```

- **Time Complexity**: O(N * S) where `S` is the total sum of `nums`.
- **Space Complexity**: O(N * S) for memoization.

---

## **3. Partition Equal Subset Sum**

### **Problem Statement**
Given an integer array `nums`, determine if it can be partitioned into two subsets with equal sum.

### **Approach**
The problem reduces to checking if there exists a subset with sum equal to **sum(nums) / 2**. If the sum is odd, return `False`.

### **Optimized DP Solution**

```python
from typing import List

def can_partition(nums: List[int]) -> bool:
    """
    Determine if a list can be partitioned into two subsets with equal sum.

    Args:
        nums (List[int]): List of numbers.

    Returns:
        bool: True if the list can be partitioned, otherwise False.
    """
    n = len(nums)
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    prev = [False] * (target + 1)
    curr = [False] * (target + 1)
    prev[0] = True
    curr[0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                curr[j] = prev[j - nums[i - 1]]
            else:
                curr[j] = False    
            curr[j] = curr[j] or prev[j]
        
        prev = curr[:]
    
    return curr[target]
```

- **Time Complexity**: O(N * S) where `S` is half the sum of `nums`.
- **Space Complexity**: O(S) using two arrays.

---

## **Conclusion**

- **Target Sum**:
  - Used a DP-based approach to count valid expressions.
  - Reduced problem to a variation of subset sum.

- **Partition Equal Subset Sum**:
  - Solved using a bottom-up DP approach with space optimization.
  - Used subset sum variation to check feasibility.

These problems strengthen our **subset sum DP skills** and help us understand **decision-based DP** techniques. Keep practicing, and see you in the next challenge! 🚀
