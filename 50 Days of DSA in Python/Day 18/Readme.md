# **Day 18: Dynamic Programming - Kadane's Algorithm & Maximum Product Subarray**

Welcome to Day 18 of **50 Days of DSA in Python**! Today, we focus on two crucial problems in dynamic programming: **Kadane's Algorithm (Maximum Subarray Sum)** and **Maximum Product Subarray**. These problems appear frequently in coding interviews and are fundamental to understanding array-based dynamic programming approaches.

---

### **Topics Covered:**
- Dynamic Programming
- Kadane's Algorithm - Maximum Subarray
- Maximum Product Subarray

---

## **1. Kadane's Algorithm - Maximum Subarray**

### **Problem Statement**
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

### **Approaches**

#### **1. Brute Force Approach (O(n²))**
The brute force approach considers all possible subarrays and computes their sums, keeping track of the maximum sum encountered.

#### **Code:**
```python
def max_subarray_brute_force(nums):
    """
    Find the maximum subarray sum using brute force.
    
    Args:
        nums (list): List of integers.
    
    Returns:
        int: Maximum subarray sum.
    """
    max_sum = float('-inf')
    n = len(nums)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum
```

---

#### **2. Kadane's Algorithm (O(n))**
Kadane’s Algorithm uses dynamic programming to keep track of the maximum subarray sum ending at each index and updates a global maximum.

#### **Code:**
```python
def max_subarray_kadane(nums):
    """
    Find the maximum subarray sum using Kadane's Algorithm.
    
    Args:
        nums (list): List of integers.
    
    Returns:
        int: Maximum subarray sum.
    """
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

---

## **2. Maximum Product Subarray**

### **Problem Statement**
Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product and return its product.

### **Approaches**

#### **1. Brute Force Approach (O(n²))**
Similar to the brute force approach for maximum subarray sum, this approach calculates the product of all possible subarrays and tracks the maximum product.

#### **Code:**
```python
def max_product_subarray_brute_force(nums):
    """
    Find the maximum product subarray using brute force.
    
    Args:
        nums (list): List of integers.
    
    Returns:
        int: Maximum product subarray.
    """
    max_product = float('-inf')
    n = len(nums)
    
    for i in range(n):
        current_product = 1
        for j in range(i, n):
            current_product *= nums[j]
            max_product = max(max_product, current_product)
    
    return max_product
```

---

#### **2. Dynamic Programming Approach (O(n))**
This approach keeps track of both the maximum and minimum products ending at each index, since a negative number can turn a small product into a large one.

#### **Code:**
```python
def max_product_subarray(nums):
    """
    Find the maximum product subarray using dynamic programming.
    
    Args:
        nums (list): List of integers.
    
    Returns:
        int: Maximum product subarray.
    """
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result
```

---

### **Conclusion**

Today, we covered two fundamental array problems in dynamic programming:
1. **Maximum Subarray Sum** using brute force and **Kadane’s Algorithm**.
2. **Maximum Product Subarray** using brute force and an **optimized dynamic programming approach**.

Understanding these problems will help in solving many real-world and competitive programming challenges related to array optimizations. Keep practicing, and see you tomorrow!