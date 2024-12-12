# Day 9: Dynamic Programming and Fibonacci Problems

Welcome to Day 9 of **55 Days of DSA in Python**! Today, we delve into the fascinating world of **Dynamic Programming**. By solving the **Fibonacci problem** using four different approaches and tackling the **Climbing Stairs problem**, we explore the systematic strategies for optimizing recursive solutions.
---

### **Topics Covered:**
- Dynamic Programming
- Fibonacci
- Climbing Stairs

---

## **1. Dynamic Programming**

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. It is particularly useful for optimization problems where solutions can be built incrementally by solving overlapping subproblems.

### **Key Concepts of Dynamic Programming**

#### **What is Dynamic Programming?**
Dynamic Programming is an optimization technique that uses **recursion** combined with **storage** to improve the performance of solving overlapping subproblems.

#### **Why Use Dynamic Programming?**
- **Avoid Redundancy**: Repeated computations in recursion are stored to save time.
- **Optimization**: Helps find the best solution among various possibilities.
- **Overlapping Subproblems**: Problems that can be broken into smaller overlapping parts benefit from DP.

#### **Core Elements of Dynamic Programming**
1. **Optimal Substructure**:
   - A problem exhibits optimal substructure if its solution can be constructed from solutions of its subproblems.
   - Example: The Fibonacci sequence can be broken into smaller Fibonacci calculations.

2. **Overlapping Subproblems**:
   - Problems where subproblems recur multiple times during recursion.
   - Example: Fibonacci involves multiple redundant calls for the same value.

#### **Dynamic Programming = Recursion + Storage = Memorization**
- **Recursion**: Solve the problem in terms of subproblems.
- **Storage**: Save the results of solved subproblems to avoid redundant calculations. This can be achieved through:
  - **Memoization**: Top-down approach (store results during recursion).
  - **Tabulation**: Bottom-up approach (iteratively calculate results and store them).

#### **Steps to Solve Problems Using Dynamic Programming**
1. **Identify the Problem Type**:
   - Check for overlapping subproblems and optimal substructure.
2. **Define the State**:
   - Create a DP array or hash table to store intermediate results.
3. **Base Cases**:
   - Define the simplest cases directly.
4. **Recursive Relation**:
   - Derive the relation to compute the state using previous states.
5. **Compute Results**:
   - Use either memoization or tabulation to find the solution.

---

## **2. Fibonacci Problem**

The Fibonacci sequence is a classic example to understand recursion and dynamic programming. The sequence is defined as:

\[
F(n) = F(n-1) + F(n-2) \text{ for } n \geq 2 \text{, and } F(0) = 0, F(1) = 1.
\]

We solve this problem using four approaches:

### **1. Recursion Approach**

```python
# Solution 1: Fibonacci using Recursion

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Parameters:
    n (int): The position of the Fibonacci number to compute.

    Returns:
    int: The nth Fibonacci number.

    Time Complexity: O(2^n) - Exponential growth due to redundant calculations.
    Space Complexity: O(n) - Stack space used for recursive calls.
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

#### **Analysis**:
- This approach is straightforward but highly inefficient due to overlapping subproblems.

---

### **2. Memorization Approach**

```python
# Solution 2: Fibonacci using Memorization

# Hash table to store previously computed Fibonacci values
ht = {0: 0, 1: 1}

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion with memorization.

    Parameters:
    n (int): The position of the Fibonacci number to compute.

    Returns:
    int: The nth Fibonacci number.

    Time Complexity: O(n) - Each Fibonacci number is computed once.
    Space Complexity: O(n) - Space required for the hash table.
    """
    if n in ht:
        return ht[n]

    ht[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return ht[n]
```

#### **Analysis**:
- Memorization eliminates redundant calculations, significantly improving efficiency.

---

### **3. Tabulation Approach**

```python
# Solution 3: Fibonacci using Tabulation

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using the tabulation approach.

    Parameters:
    n (int): The position of the Fibonacci number to compute.

    Returns:
    int: The nth Fibonacci number.

    Time Complexity: O(n) - Each Fibonacci number is computed once iteratively.
    Space Complexity: O(n) - Space required for the DP array.
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

#### **Analysis**:
- Tabulation solves the problem iteratively, avoiding recursion altogether.

---

### **4. Space Optimization Approach**

```python
# Solution 4: Fibonacci using Space Optimization

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using space optimization.

    Parameters:
    n (int): The position of the Fibonacci number to compute.

    Returns:
    int: The nth Fibonacci number.

    Time Complexity: O(n) - Each Fibonacci number is computed once iteratively.
    Space Complexity: O(1) - Only two variables are used for storage.
    """
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr
```

#### **Analysis**:
- This approach is the most efficient in terms of space while maintaining linear time complexity.

---

## **3. Climbing Stairs Problem**

The **Climbing Stairs** problem asks us to find the number of distinct ways to climb to the top of a staircase with \( n \) steps, where each time you can climb 1 or 2 steps.

### **Problem Statement**
Given \( n \), calculate the number of ways to reach the top.

### **Solution: Recursion Approach**

```python
# Solution: Climbing Stairs using Recursion Approach

def climbStairs(n):
    """
    Calculate the number of distinct ways to climb to the top of a staircase with `n` steps.

    Parameters:
    n (int): The total number of steps in the staircase.

    Returns:
    int: The number of distinct ways to climb to the top.

    Time Complexity: O(2^n) - Exponential growth due to redundant calculations.
    Space Complexity: O(n) - Stack space used for recursive calls.
    """
    if n <= 2:
        return n

    def helper(first, second, n, curr):
        """
        Recursive helper function to compute the number of ways.

        Parameters:
        first (int): Number of ways to reach the step before the current step.
        second (int): Number of ways to reach the current step.
        n (int): Total number of steps.
        curr (int): Current step being evaluated.

        Returns:
        int: Number of ways to reach the nth step.
        """
        next_num = first + second

        if curr == n:
            return next_num

        return helper(second, next_num, n, curr + 1)

    return helper(1, 2, n, 3)
```

#### **Analysis**:
- Similar to the Fibonacci sequence, this problem can be optimized using memorization or tabulation.

---

* ## **Conclusion**  
- **Dynamic Programming**:  
  - Combines recursion and storage (memoization) to optimize problem-solving.  
  - Tabulation and space optimization techniques further improve performance and reduce memory usage.  

- **Fibonacci Series**:  
  - Explored through four approaches: recursion, memoization, tabulation, and space optimization.  
  - Showcased the gradual improvement in efficiency with each approach.  

- **Climbing Stairs**:  
  - Solved using a recursive helper function.  
  - Illustrated dynamic programming concepts by breaking the problem into overlapping subproblems and utilizing recursion with backtracking.  