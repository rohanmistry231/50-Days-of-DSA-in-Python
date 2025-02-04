# **Day 28: Searching**

Welcome to Day 28 of **50 Days of DSA in Python**! Today, we will focus on **Searching**, particularly **Binary Search** and **Search in Rotated Sorted Array**.

---

### **Topics Covered:**
- Searching  
- Binary Search  
- Search in Rotated Sorted Array  

---

## **1. Binary Search**

### **Problem Statement**  
Given a sorted array of integers, write a function to search for a target value. If the target exists in the array, return its index; otherwise, return `-1`.

### **Approaches**

#### **1. Binary Search (Efficient Search)**

Binary Search works on a sorted array by repeatedly dividing the search interval in half. If the value of the target is less than the value at the middle index, it narrows the search to the left half, otherwise, it narrows the search to the right half.

#### **Code:**
```python
def binarySearch(nums, target):
    """
    Perform binary search to find the target value in a sorted array.

    Args:
        nums (list): A sorted list of integers.
        target (int): The target value to search for.

    Returns:
        int: The index of the target value, or -1 if not found.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
```

---

## **2. Search in Rotated Sorted Array**

### **Problem Statement**  
You are given a rotated sorted array. You need to search for a target value in the array. If the target exists, return its index; otherwise, return `-1`. The array was originally sorted in ascending order but then rotated at some unknown pivot.

### **Approaches**

#### **1. Modified Binary Search**

Since the array is rotated, the array can still be divided into two sorted subarrays. We can apply a modified binary search to determine which part of the array to search in, by comparing the middle element with the leftmost and rightmost elements.

#### **Code:**
```python
def search(nums, target):
    """
    Search for the target value in a rotated sorted array.

    Args:
        nums (list): A rotated sorted list of integers.
        target (int): The target value to search for.

    Returns:
        int: The index of the target value, or -1 if not found.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        
        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

---

### **Conclusion**

Today, we explored two important searching techniques:

1. **Binary Search**: We applied binary search to find a target in a sorted array, reducing the time complexity to `O(log n)`.
2. **Search in Rotated Sorted Array**: We modified the binary search algorithm to handle rotated arrays, efficiently finding the target in `O(log n)` time.

These searching techniques are fundamental for solving many problems in various domains, including databases, data retrieval, and computational geometry. Keep practicing, and see you tomorrow!