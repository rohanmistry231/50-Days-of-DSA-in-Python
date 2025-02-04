# **Day 20: Greedy Algorithms - Jump Game & Minimum Arrows to Burst Balloons**

Welcome to Day 20 of **50 Days of DSA in Python**! Today, we continue exploring **Greedy Algorithms** by solving two important problems: **Jump Game 1** and **Minimum Number of Arrows to Burst Balloons**. These problems are frequently encountered in coding interviews and demonstrate the efficiency of greedy strategies.

---

### **Topics Covered:**
- Greedy Algorithms
- Jump Game 1
- Minimum Number of Arrows to Burst Balloons

---

## **1. Jump Game 1**

### **Problem Statement**
Given an array `nums` where `nums[i]` represents the maximum number of steps that can be taken forward from index `i`, determine if it is possible to reach the last index starting from index `0`.

### **Approach: Greedy Strategy (O(n))**
1. Maintain a variable `max_reach` to track the farthest index that can be reached.
2. Iterate through the array, updating `max_reach` at each step.
3. If `max_reach` ever becomes greater than or equal to the last index, return `True`.
4. If we reach an index that is not accessible, return `False`.

### **Code:**
```python
from typing import List

def can_jump(nums: List[int]) -> bool:
    """
    Determines if it is possible to reach the last index.
    
    Args:
        nums (list): List of integers representing jump distances.
    
    Returns:
        bool: True if reachable, False otherwise.
    """
    max_reach = 0
    n = len(nums)
    
    for i in range(n):
        if i > max_reach:
            return False  # Can't move past this point
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= n - 1:
            return True  # Can reach or exceed the last index
    
    return False
```

---

## **2. Minimum Number of Arrows to Burst Balloons**

### **Problem Statement**
Given an array `points` where each `points[i] = [x_start, x_end]` represents a balloon with horizontal spread, find the **minimum number of arrows** required to burst all balloons. An arrow can burst all balloons whose spread overlaps at the same point.

### **Approach: Greedy Strategy (O(n log n))**
1. **Sort** the balloons by their **ending coordinate**.
2. Use a greedy approach to track the last position where an arrow was shot.
3. If the next balloon starts after the last shot, shoot a new arrow and update the shooting position.
4. Continue until all balloons are burst.

### **Code:**
```python
from typing import List

def min_arrows_to_burst_balloons(points: List[List[int]]) -> int:
    """
    Finds the minimum number of arrows required to burst all balloons.
    
    Args:
        points (list): List of balloon intervals [x_start, x_end].
    
    Returns:
        int: Minimum number of arrows needed.
    """
    if not points:
        return 0
    
    # Sort balloons by end position
    points.sort(key=lambda x: x[1])
    
    arrows = 1
    last_arrow_pos = points[0][1]
    
    for start, end in points[1:]:
        if start > last_arrow_pos:
            arrows += 1
            last_arrow_pos = end
    
    return arrows
```

---

### **Conclusion**

Today, we explored two essential greedy problems:
1. **Jump Game 1** - Using a greedy approach to determine if we can reach the last index.
2. **Minimum Number of Arrows to Burst Balloons** - Using sorting and a greedy strategy to minimize the number of arrows needed.

Greedy algorithms help solve many optimization problems efficiently. Keep practicing, and see you tomorrow!