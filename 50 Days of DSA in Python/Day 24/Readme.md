# **Day 24: Arrays**

Welcome to Day 24 of **50 Days of DSA in Python**! Today, we will focus on two important problems involving **Arrays**: **Rotate Array** and **Container with Most Water**. Both problems are excellent exercises in array manipulation and optimization.

---

### **Topics Covered:**
- Arrays  
- Rotate Array  
- Container with Most Water  

---

## **1. Rotate Array**

### **Problem Statement**  
Given an array `nums`, rotate the array to the right by `k` steps, where `k` is a non-negative integer.

### **Approaches**

#### **1. Brute Force Approach**

The brute force approach involves shifting each element of the array `k` positions to the right. We can do this by using a temporary array or directly manipulating the array.

#### **Code:**
```python
def rotate(nums, k):
    """
    Rotate the array to the right by k steps.

    Args:
        nums (list): The list of integers to rotate.
        k (int): The number of positions to rotate.

    Returns:
        None: The function modifies the list in-place.
    """
    n = len(nums)
    k = k % n  # Handle cases where k is greater than the length of the array
    nums[:] = nums[-k:] + nums[:-k]
```

---

## **2. Container with Most Water**

### **Problem Statement**  
Given an array of integers `height` representing the height of walls, where each element represents the height of a vertical line, find two lines that together with the x-axis form a container that holds the most water. Return the maximum amount of water a container can store.

### **Approaches**

#### **1. Two Pointer Approach**

The optimal solution uses the two-pointer technique. We initialize two pointers, one at the start and one at the end of the array, and calculate the area between them. We then move the pointer that points to the shorter line towards the center, aiming to maximize the area at each step.

#### **Code:**
```python
def maxArea(height):
    """
    Calculate the maximum area that can be formed between two lines.

    Args:
        height (list): A list of integers representing the heights of lines.

    Returns:
        int: The maximum area formed by any two lines.
    """
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the area between the current pair of lines
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

---

### **Conclusion**

Today, we tackled two interesting **Array** problems:

1. **Rotate Array**: Rotating an array by `k` steps using efficient methods.
2. **Container with Most Water**: Maximizing the area between two lines using the two-pointer technique.

Arrays are a fundamental data structure, and these problems are great exercises to improve your understanding of array manipulation and optimization. Keep practicing, and see you tomorrow!