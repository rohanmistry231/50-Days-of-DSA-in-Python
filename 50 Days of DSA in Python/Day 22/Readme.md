# **Day 22: Greedy Algorithms**

Welcome to Day 22 of **50 Days of DSA in Python**! Today, we dive into **Greedy Algorithms**, focusing on two key problems: **Task Scheduler** and **Largest Number**. Greedy algorithms are used to solve optimization problems by making the locally optimal choice at each stage, with the hope of finding a global optimum.

---

### **Topics Covered:**
- Greedy Algorithms  
- Task Scheduler  
- Largest Number  

---

## **1. Task Scheduler**

### **Problem Statement**  
Given a list of tasks with their frequencies and an integer `n` representing the cooldown time between the same task, determine the least number of units of time required to finish all tasks. You must schedule the tasks such that the same tasks are not executed within `n` units of time.

### **Approaches**

#### **1. Greedy Approach**

The greedy approach involves scheduling tasks with the highest frequency first, placing them at intervals that respect the cooldown period.

#### **Code:**
```python
import heapq

def leastInterval(tasks, n):
    """
    Calculate the least number of intervals needed to schedule all tasks.

    Args:
        tasks (list): A list of task characters.
        n (int): The cooldown period between the same task.

    Returns:
        int: The least number of intervals needed to schedule all tasks.
    """
    if not tasks:
        return 0
    
    # Count the frequency of each task
    task_count = {}
    for task in tasks:
        task_count[task] = task_count.get(task, 0) + 1
    
    # Max-heap to store the frequency of tasks
    max_heap = [-count for count in task_count.values()]
    heapq.heapify(max_heap)

    time = 0
    while max_heap:
        temp = []
        for _ in range(n + 1):
            if max_heap:
                count = heapq.heappop(max_heap) + 1  # Decrease the count
                if count != 0:
                    temp.append(count)
            
        for item in temp:
            heapq.heappush(max_heap, item)

        time += n + 1 if max_heap else len(temp)

    return time
```

---

## **2. Largest Number**

### **Problem Statement**  
Given a list of non-negative integers `nums`, arrange them such that they form the largest possible number. The result should be returned as a string.

### **Approaches**

#### **1. Greedy Approach (Custom Sorting)**

The greedy approach involves sorting the numbers based on their lexicographical order when concatenated, to form the largest possible number.

#### **Code:**
```python
from functools import cmp_to_key

def largestNumber(nums):
    """
    Arrange numbers to form the largest possible number.

    Args:
        nums (list): A list of non-negative integers.

    Returns:
        str: The largest number formed by concatenating the integers.
    """
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        return 0

    # Convert all integers to strings for custom sorting
    nums = list(map(str, nums))
    nums.sort(key=cmp_to_key(compare))
    
    # If the largest number is 0, return "0"
    return ''.join(nums) if nums[0] != '0' else '0'
```

---

### **Conclusion**

Today, we explored two important problems that can be solved using **Greedy Algorithms**:

1. **Task Scheduler**: Scheduling tasks optimally to minimize idle time using a greedy approach.
2. **Largest Number**: Forming the largest number possible by sorting the numbers using a custom comparison function.

Greedy algorithms provide an efficient way to solve optimization problems, but it's important to understand the problem thoroughly to identify where a greedy approach is applicable. Keep practicing, and see you tomorrow!