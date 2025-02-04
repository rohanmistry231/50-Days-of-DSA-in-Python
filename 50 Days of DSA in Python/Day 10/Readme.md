# **Day 10: Dynamic Programming - Min Cost Climbing Stairs and Tribonacci**

Welcome to Day 10 of **50 Days of DSA in Python**! Today, we delve deeper into dynamic programming by tackling two classic problems: the **Min Cost Climbing Stairs** problem and the **Tribonacci** sequence problem. These problems further enhance our understanding of optimization and how dynamic programming allows us to solve problems efficiently by avoiding redundant computations.

---

### **Topics Covered:**
- Dynamic Programming
- Min Cost Climbing Stairs
- Tribonacci

---

## **1. Dynamic Programming Overview**

Dynamic programming is a powerful technique to solve optimization problems by breaking them into smaller subproblems. It combines two key ideas:

1. **Recursion**: Breaking the problem into smaller subproblems.
2. **Storage (Memoization/Tabulation)**: Storing the results of already solved subproblems to avoid redundant computations.

### **Key Concepts**
- **Memoization**: Storing results of subproblems in a top-down manner.
- **Tabulation**: Building the solution iteratively in a bottom-up manner.
- **Optimization**: Reducing space complexity by reusing variables instead of maintaining large tables.

---

## **2. Min Cost Climbing Stairs**

### **Problem Statement**
You are given an array `cost` where `cost[i]` is the cost of stepping on the `i-th` stair. Once you pay the cost, you can climb one or two steps. Your goal is to reach the top of the staircase (beyond the last index) with the minimum cost.

### **Approaches**

#### **1. Recursion**

The recursive approach involves solving the problem by considering the two possible moves at each step:
- Climb one step.
- Climb two steps.

#### **Code**
```python
from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    """
    Calculate the minimum cost to reach the top of the stairs using recursion.

    Args:
        cost (List[int]): The cost of each step.

    Returns:
        int: The minimum cost to reach the top.
    """
    n = len(cost)

    def helper(index: int) -> int:
        # Base case: If index is beyond the stairs, no cost is needed
        if index >= n:
            return 0

        # Climb one step or two steps
        climb_one = cost[index] + helper(index + 1)
        climb_two = cost[index] + helper(index + 2)

        return min(climb_one, climb_two)

    return min(helper(0), helper(1))

# Time Complexity: O(2^n) - Due to overlapping subproblems.
# Space Complexity: O(n) - Recursion stack.
```

#### **2. Memoization**

In this approach, we optimize the recursive solution by storing the results of subproblems in an array, avoiding redundant computations.

#### **Code**
```python
from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    """
    Calculate the minimum cost to reach the top of the stairs using memoization.

    Args:
        cost (List[int]): The cost of each step.

    Returns:
        int: The minimum cost to reach the top.
    """
    n = len(cost)
    memo = [-1] * n

    def helper(index: int) -> int:
        # Base case: If index is beyond the stairs, no cost is needed
        if index >= n:
            return 0

        # Return already computed value
        if memo[index] != -1:
            return memo[index]

        # Climb one step or two steps
        climb_one = cost[index] + helper(index + 1)
        climb_two = cost[index] + helper(index + 2)

        memo[index] = min(climb_one, climb_two)
        return memo[index]

    return min(helper(0), helper(1))

# Time Complexity: O(n) - Each index is processed once.
# Space Complexity: O(n) - For memoization array and recursion stack.
```

#### **3. Tabulation**

The tabulation approach builds the solution iteratively by filling a table of results from the base case up to the desired result.

#### **Code**
```python
from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    """
    Calculate the minimum cost to reach the top of the stairs using tabulation.

    Args:
        cost (List[int]): The cost of each step.

    Returns:
        int: The minimum cost to reach the top.
    """
    n = len(cost)
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        climb_one = cost[i - 1] + dp[i - 1]
        climb_two = cost[i - 2] + dp[i - 2]
        dp[i] = min(climb_one, climb_two)

    return dp[n]

# Time Complexity: O(n) - Single iteration through the array.
# Space Complexity: O(n) - For the DP array.
```

---

## **3. Tribonacci**

### **Problem Statement**
The Tribonacci sequence is defined as follows:
- T(0) = 0, T(1) = 1, T(2) = 1
- T(n) = T(n-1) + T(n-2) + T(n-3) for n >= 3

The task is to compute the `n-th` Tribonacci number efficiently.

#### **Approach: Space Optimization**

In this approach, we only maintain variables for the last three numbers in the sequence, reducing the space complexity to O(1).

#### **Code**
```python
from typing import List

def tribonacci(n: int) -> int:
    """
    Calculate the n-th Tribonacci number using space optimization.

    Args:
        n (int): The index of the Tribonacci number to compute.

    Returns:
        int: The n-th Tribonacci number.
    """
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    trib_n_minus_3, trib_n_minus_2, trib_n_minus_1 = 0, 1, 1

    for i in range(3, n + 1):
        trib_n = trib_n_minus_3 + trib_n_minus_2 + trib_n_minus_1
        trib_n_minus_3, trib_n_minus_2, trib_n_minus_1 = trib_n_minus_2, trib_n_minus_1, trib_n

    return trib_n

# Time Complexity: O(n) - Single iteration through the sequence.
# Space Complexity: O(1) - Constant space used.
```

---

## **Conclusion**

- **Min Cost Climbing Stairs**:
  - Demonstrated three approaches: Recursion, Memoization, and Tabulation.
  - Optimized the solution step-by-step, reducing time and space complexity.

- **Tribonacci**:
  - Solved the problem using a space-optimized approach, maintaining only the last three numbers of the sequence.