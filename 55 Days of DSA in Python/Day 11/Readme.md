# **Day 11: Dynamic Programming - 01 Knapsack and Unbounded Knapsack**

Welcome to Day 11 of **55 Days of DSA in Python**! Today, we focus on two classic problems in Dynamic Programming: the **01 Knapsack Problem** and the **Unbounded Knapsack Problem**. These problems introduce us to optimization techniques that allow us to make decisions about including or excluding items to maximize value, while respecting the given weight constraints.

---

### **Topics Covered:**
- Dynamic Programming
- 01 Knapsack Problem
- Unbounded Knapsack Problem

---

## **1. Dynamic Programming Overview**

Dynamic programming (DP) is a powerful technique used to solve optimization problems. By breaking the problem into smaller subproblems, it ensures that each subproblem is solved only once, storing the results to avoid redundant calculations.

The primary techniques in DP are:
- **Memoization (Top-down approach)**: Solving the problem recursively and storing the results of subproblems.
- **Tabulation (Bottom-up approach)**: Building the solution iteratively by filling up a table.
- **Space Optimization**: Reducing the space complexity by storing only the essential results.

---

## **2. 01 Knapsack Problem**

### **Problem Statement**
You are given `n` items, each with a weight and a value. You have a knapsack that can hold a maximum weight `W`. The task is to determine the maximum value of items that can be placed in the knapsack without exceeding the weight limit.

### **Approaches**

#### **1. Recursive Approach**

In this approach, the function recursively checks whether to include each item or exclude it, exploring both possibilities at each step.

#### **Code:**
```python
def knap_sack(W, wt, val, n):
    """
    Solve the 0/1 Knapsack problem using recursion.

    Args:
        W (int): The maximum weight capacity of the knapsack.
        wt (list[int]): A list of weights of the items.
        val (list[int]): A list of values of the items.
        n (int): The total number of items.

    Returns:
        int: The maximum value that can be obtained within the weight limit.
    """
    
    def helper(index, rem_weight):
        # Base case
        if index >= n or rem_weight == 0:
            return 0

        # Exclude the current item
        exclude = helper(index + 1, rem_weight)
        
        # Include the current item, if it fits in the remaining weight
        include = 0
        if wt[index] <= rem_weight:
            include = val[index] + helper(index + 1, rem_weight - wt[index])

        return max(exclude, include)

    return helper(0, W)
```

#### **2. Memoization Approach**

Here, the recursive approach is enhanced with memoization, which stores the results of subproblems to avoid redundant computations.

#### **Code:**
```python
def knap_sack(W, wt, val, n):
    """
    Solve the 0/1 Knapsack problem using memoization.

    Args:
        W (int): The maximum weight capacity of the knapsack.
        wt (list[int]): A list of weights of the items.
        val (list[int]): A list of values of the items.
        n (int): The total number of items.

    Returns:
        int: The maximum value that can be obtained within the weight limit.
    """
    
    dp = [[-1] * (W + 1) for _ in range(n)]
    
    def helper(index, rem_weight):
        # Base case
        if index >= n or rem_weight == 0:
            return 0
        
        # Return already computed value
        if dp[index][rem_weight] != -1:
            return dp[index][rem_weight]
        
        # Exclude the current item
        exclude = helper(index + 1, rem_weight)
        
        # Include the current item, if it fits in the remaining weight
        include = 0
        if wt[index] <= rem_weight:
            include = val[index] + helper(index + 1, rem_weight - wt[index])

        dp[index][rem_weight] = max(exclude, include)
        return dp[index][rem_weight]

    return helper(0, W)
```

#### **3. Tabulation Approach**

In this approach, we use an iterative bottom-up approach where we fill a DP table from the base case to the solution.

#### **Code:**
```python
def knap_sack(W, wt, val, n):
    """
    Solve the 0/1 Knapsack problem using tabulation.

    Args:
        W (int): The maximum weight capacity of the knapsack.
        wt (list[int]): A list of weights of the items.
        val (list[int]): A list of values of the items.
        n (int): The total number of items.

    Returns:
        int: The maximum value that can be obtained within the weight limit.
    """
    
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            # Exclude the current item
            exclude = dp[i - 1][j]
            
            # Include the current item, if it fits in the remaining weight
            include = 0
            if wt[i - 1] <= j:
                include = val[i - 1] + dp[i - 1][j - wt[i - 1]]
            
            dp[i][j] = max(exclude, include)
    
    return dp[n][W]
```

#### **4. Space Optimized Tabulation Approach**

In this space-optimized version, only two arrays (`prev` and `curr`) are used to store results, reducing space complexity from O(n * W) to O(W).

#### **Code:**
```python
def knap_sack(W, wt, val, n):
    """
    Solve the 0/1 Knapsack problem using space-optimized tabulation.

    Args:
        W (int): The maximum weight capacity of the knapsack.
        wt (list[int]): A list of weights of the items.
        val (list[int]): A list of values of the items.
        n (int): The total number of items.

    Returns:
        int: The maximum value that can be obtained within the weight limit.
    """
    
    prev = [0] * (W + 1)
    curr = [0] * (W + 1)

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            # Exclude the current item
            exclude = prev[j]
            
            # Include the current item, if it fits in the remaining weight
            include = 0
            if wt[i - 1] <= j:
                include = val[i - 1] + prev[j - wt[i - 1]]
            
            curr[j] = max(exclude, include)
        
        # Update prev to be the current row after each iteration
        prev = curr[:]
    
    return curr[W]
```

---

## **3. Unbounded Knapsack Problem**

### **Problem Statement**
In the Unbounded Knapsack problem, each item can be chosen multiple times to maximize the total value of items that can be placed in the knapsack, such that the total weight does not exceed the given weight limit.

### **Approach: Tabulation**

In this approach, we use a DP table where each entry represents the maximum value that can be obtained for each weight capacity, considering the possibility of including each item multiple times.

#### **Code:**
```python
def knap_sack(N, max_weight, values, weights):
    """
    Solve the Unbounded Knapsack problem using dynamic programming.

    Args:
        N (int): The number of items.
        max_weight (int): The maximum weight capacity of the knapsack.
        values (list[int]): A list of values of the items.
        weights (list[int]): A list of weights of the items.

    Returns:
        int: The maximum value that can be obtained within the weight limit.
    """
    
    dp = [[-1] * (max_weight + 1) for _ in range(N + 1)]
    
    for j in range(max_weight + 1):
        dp[0][j] = 0  # No items, so no value can be obtained
    
    for i in range(N + 1):
        dp[i][0] = 0  # No capacity, so no value can be obtained

    for i in range(1, N + 1):
        for j in range(1, max_weight + 1):
            exclude = dp[i - 1][j]  # Exclude current item
            include = 0
            if weights[i - 1] <= j:
                include = values[i - 1] + dp[i][j - weights[i - 1]]  # Include current item
            
            dp[i][j] = max(exclude, include)

    return dp[N][max_weight]
```

---

## **Conclusion**

- **01 Knapsack**:
  - Covered four approaches: Recursion, Memoization, Tabulation, and Space Optimized Tabulation.
  - Demonstrated how dynamic programming can optimize the solution to this classic optimization problem.

- **Unbounded Knapsack**:
  - Implemented the unbounded knapsack problem using tabulation, ensuring that each item can be used multiple times.