# Day 2: Recursion and Problem Solving

Welcome to Day 2 of **50 Days of DSA in Python**! On this day, we delved into **Recursion** and tackled two intriguing problems: **k-th Symbol in Grammar** and the **Josephus Problem**. This README is structured to provide detailed explanations and solutions for these topics.

---

## **Topics to be Covered**

- Recursion  
- k-th Symbol in Grammar  
- Josephus Problem  

---

### **1. Recursion**

#### **1. What is Recursion?**  
**Definition:**  
Recursion is a programming technique where a function calls itself to solve smaller instances of a problem until it reaches a base condition. It is often used to break down complex problems into simpler, more manageable sub-problems.  

**Example:** A recursive function to calculate the factorial of a number:  
```python
def factorial(n):
    if n == 0:  # Base condition
        return 1
    return n * factorial(n - 1)  # Recursive call
```

---

#### **2. When to Use Recursion?**  
Recursion is most useful in scenarios where a problem can naturally be divided into similar sub-problems. Examples include:  
- Solving problems with hierarchical or tree-like structures (e.g., file systems, binary trees).  
- Problems that require exploring multiple branches or possibilities (e.g., backtracking).  
- Mathematical problems (e.g., Fibonacci numbers, factorial, permutations).  

**When to avoid recursion:**  
- When the recursion depth may exceed the stack limit, causing a stack overflow.  
- If the problem can be solved more efficiently with iteration (e.g., when optimizing time complexity).  

---

#### **3. Visualization: Recursion Tree**  
A **recursion tree** visualizes the breakdown of recursive calls. Each node represents a function call, and its children represent the smaller sub-problems it solves.  

Example for Fibonacci sequence:  
To calculate `fib(4)`:  
```
fib(4)
├── fib(3)
│   ├── fib(2)
│   │   ├── fib(1)
│   │   └── fib(0)
│   └── fib(1)
└── fib(2)
    ├── fib(1)
    └── fib(0)
```

---

#### **4. Recursion Call Stack**  
The **call stack** is a data structure used by the computer to manage function calls. Each recursive function call is pushed onto the stack, and once the base condition is met, the calls are resolved (popped) in reverse order.  

Example for `factorial(3)`:  
1. Push `factorial(3)`  
2. Push `factorial(2)`  
3. Push `factorial(1)`  
4. Push `factorial(0)` → Base condition met  
5. Pop and return values step-by-step  

---

#### **5. Recursion vs Iteration**  
| Feature              | Recursion                       | Iteration                        |  
|----------------------|---------------------------------|----------------------------------|  
| **Definition**        | Function calling itself         | Repeated execution using loops   |  
| **Complexity**        | Higher space complexity due to call stack | Lower space complexity           |  
| **Suitability**       | Hierarchical problems, backtracking | Simple, repetitive tasks         |  
| **Readability**       | Often more concise, intuitive   | More verbose but often faster    |  

**Example:** Factorial using iteration:  
```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

---

#### **6. Ways to Write Base Condition**  
A **base condition** is the terminating condition for a recursive function. It prevents infinite recursion.  

**Guidelines to define a base condition:**  
1. Ensure the condition is reachable for every possible input.  
2. It should handle the smallest sub-problems (e.g., `n == 0` or `n == 1`).  

Example for sum of numbers from 1 to n:  
```python
def sum_numbers(n):
    if n == 0:  # Base condition
        return 0
    return n + sum_numbers(n - 1)  # Recursive call
```

---

#### **7. Recursive Leap of Faith**  
The **recursive leap of faith** involves assuming that the recursive call will work correctly for smaller instances of the problem. Focus on combining the result of the recursive call with the current step.  

Example:  
In the factorial example, assume that `factorial(n - 1)` works correctly and multiply it by `n`.

---

#### **8. Recurrence Relation**  
A **recurrence relation** represents a recursive function mathematically. It describes the relationship between the problem and its sub-problems.  

Example for factorial:  
- Recurrence relation: `T(n) = T(n - 1) + O(1)`  
- Base condition: `T(0) = O(1)`  

---

#### **9. Solving Recursion Questions (0 to n and n to 0)**  

**Print numbers from 0 to n:**  
```python
def print_0_to_n(n):
    if n < 0:  # Base condition
        return
    print_0_to_n(n - 1)  # Recursive call
    print(n)  # Post-recursive action
```

**Print numbers from n to 0:**  
```python
def print_n_to_0(n):
    if n < 0:  # Base condition
        return
    print(n)  # Pre-recursive action
    print_n_to_0(n - 1)  # Recursive call
```

---

### **2. k-th Symbol in Grammar**
#### **Problem Statement**
We are given two integers `n` and `k`. The first row of a grammar sequence is `0`. Each subsequent row is constructed by replacing each occurrence of `0` with `01` and each occurrence of `1` with `10`. Determine the k-th symbol in the n-th row of the sequence.

#### **Recursive Solution**
```python
def kth_symbol(n, k):
    if n == 1:
        return 0
    mid = 2 ** (n - 1) // 2
    if k <= mid:
        return kth_symbol(n - 1, k)
    else:
        return 1 - kth_symbol(n - 1, k - mid)
```

---

### **3. Josephus Problem**

The **Josephus Problem** is a famous theoretical problem in which people stand in a circle and eliminate every k-th person until only one person remains. The task is to determine the position of the last person standing.

##### **Approaches to Solve the Josephus Problem**

1. **Recursive Approach:**
   The first approach to solve the Josephus problem is by using recursion. The problem can be broken down into smaller sub-problems, where each smaller problem is a reduced version of the original. The recursive function works by removing a person in each iteration and calling the same function with the reduced problem size. Here's the recursive implementation:

   ```python
   def josephus_recursive(n, k):
       if n == 1:
           return 0
       else:
           return (josephus_recursive(n - 1, k) + k) % n
   ```

   **Time Complexity:**  
   The recursive approach has a time complexity of **O(n)**, but the recursion depth can be problematic for large values of `n` as it uses the system’s call stack.

   **Space Complexity:**  
   The space complexity is **O(n)** due to the call stack used by recursion.

2. **Optimized Recursive Approach (Tail Recursion):**
   In this approach, we apply **tail recursion** to optimize the solution. Tail recursion can be optimized by the compiler to avoid using extra stack space.

   ```python
   def josephus_optimized(n, k, result=0):
       if n == 1:
           return result
       else:
           result = (result + k) % n
           return josephus_optimized(n - 1, k, result)
   ```

   **Time Complexity:**  
   The time complexity remains **O(n)**.

   **Space Complexity:**  
   The space complexity can be reduced to **O(1)** in case the tail recursion is optimized by the compiler.

3. **Iterative Approach:**
   In this approach, instead of using recursion, we solve the problem iteratively. We can calculate the position of the last remaining person by iterating over all the people, adjusting the result at each step. This avoids the overhead associated with recursion and is more efficient for large values of `n`.

   ```python
   def josephus_iterative(n, k):
       result = 0
       for i in range(2, n + 1):
           result = (result + k) % i
       return result
   ```

   **Time Complexity:**  
   The time complexity of the iterative approach is **O(n)**.

   **Space Complexity:**  
   The space complexity is **O(1)** as we do not need extra space for recursive calls.

##### **Complexity Improvements Across Approaches**

- **Recursive Approach:** The initial approach has a time complexity of **O(n)** and a space complexity of **O(n)** due to the recursive call stack.
- **Optimized Recursive Approach:** By applying tail recursion, we can reduce the space complexity to **O(1)** while maintaining the time complexity at **O(n)**.
- **Iterative Approach:** The iterative approach improves the space complexity to **O(1)**, while still retaining the **O(n)** time complexity, making it the most efficient solution for large inputs.

---

### **Conclusion**

In **Day 2**, we covered the following topics:

- **Recursion**: We explored the concept of recursion, understanding its definition, when to use it, and how to implement it effectively. We also discussed its comparison with iteration and the importance of base conditions and the recursion tree. Recursion is a powerful technique, especially in hierarchical and backtracking problems, but we need to be mindful of its potential inefficiency in terms of space complexity. We also looked at how recursion could be optimized in some cases, reducing its complexity.

- **k-th Symbol in Grammar**: We learned how to find the k-th symbol in a grammar, breaking the problem down into a recursive structure. This is a great example of using recursion for a problem involving fractal-like behavior and patterns, reinforcing how recursion can simplify complex problems.

- **Josephus Problem**: This problem was solved using three approaches:
  1. **Recursive Approach**: We implemented the basic recursive solution, which works well for small input sizes but suffers from a high space complexity due to recursive calls.
  2. **Optimized Recursive Approach**: We improved the recursive approach by using tail recursion, which reduced the space complexity from O(n) to O(1) while maintaining the same time complexity.
  3. **Iterative Approach**: Finally, we implemented an iterative solution, which is the most efficient in terms of space complexity (O(1)) and still runs in O(n) time. This approach is the preferred method for larger inputs.

Throughout these problems, we not only applied recursion but also explored how to optimize and choose between recursive and iterative solutions. Understanding these techniques will help us solve a variety of algorithmic problems efficiently and effectively. As we progress, we will continue to build on these concepts to tackle even more complex challenges.