# **Day 29: Searching**

Welcome to Day 29 of **50 Days of DSA in Python**! Today, we will dive deeper into **Searching**, with a focus on **Finding the First and Last Position of an Element** and **Searching in a 2D Array**.

---

### **Topics Covered:**
- Searching  
- Find First and Last Position  
- Search in 2D Array  

---

## **1. Find First and Last Position**

### **Problem Statement**  
Given a sorted array of integers and a target value, find the first and last positions of the target value in the array. If the target is not found, return `[-1, -1]`.

### **Approaches**

#### **1. Binary Search for First and Last Position**

We can use binary search twice: first to find the first occurrence of the target, and then to find the last occurrence. This ensures that we can find the positions in `O(log n)` time.

#### **Code:**
```python
def searchRange(nums, target):
    """
    Find the first and last position of the target in a sorted array.

    Args:
        nums (list): A sorted list of integers.
        target (int): The target value to search for.

    Returns:
        list: A list with the first and last positions of the target value.
    """
    
    def findLeft():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def findRight():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    left, right = findLeft(), findRight()
    
    if left <= right:
        return [left, right]
    return [-1, -1]
```

---

## **2. Search in 2D Array**

### **Problem Statement**  
You are given a 2D matrix in which each row is sorted in ascending order, and the first integer of each row is greater than the last integer of the previous row. Given a target integer, write a function to search the target in the matrix. Return `True` if the target exists in the matrix, otherwise return `False`.

### **Approaches**

#### **1. Binary Search on the Entire Matrix**

Since each row and each column of the matrix is sorted, we can treat the matrix as a 1D sorted array and apply binary search. We can compute the index of a cell in the matrix as if the matrix is flattened.

#### **Code:**
```python
def searchMatrix(matrix, target):
    """
    Search for the target value in a 2D matrix.

    Args:
        matrix (list of list): A 2D matrix where each row is sorted.
        target (int): The target value to search for.

    Returns:
        bool: True if the target is found in the matrix, False otherwise.
    """
    if not matrix:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = matrix[mid // cols][mid % cols]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False
```

---

### **Conclusion**

Today, we learned how to perform efficient searching in two distinct problems:

1. **Find First and Last Position**: By utilizing binary search, we were able to find the first and last occurrences of a target value in a sorted array in `O(log n)` time.
2. **Search in 2D Array**: We extended binary search to handle 2D matrices, enabling us to search for a target in a sorted matrix in `O(log m * n)` time, where `m` is the number of rows and `n` is the number of columns.

These searching techniques are crucial for handling large datasets efficiently. Keep practicing these methods, and see you tomorrow!