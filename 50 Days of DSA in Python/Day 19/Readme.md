# **Day 19: Greedy Algorithms - Fractional Knapsack & Non-overlapping Intervals**

Welcome to Day 19 of **50 Days of DSA in Python**! Today, we explore **Greedy Algorithms** and apply them to two classic problems: **Fractional Knapsack** and **Non-overlapping Intervals**. These problems frequently appear in coding interviews and demonstrate the power of greedy strategies.

---

## **Introduction to Greedy Algorithms**

### **What are Greedy Algorithms?**
A **Greedy Algorithm** is a problem-solving approach that makes the locally optimal choice at each stage with the hope of finding a global optimum. Greedy algorithms do not always yield an optimal solution for all problems but are highly effective for specific types of optimization problems.

### **Key Characteristics of Greedy Algorithms:**
1. **Greedy Choice Property** - The optimal solution can be built by making locally optimal choices.
2. **Optimal Substructure** - A problem exhibits optimal substructure if an optimal solution to the entire problem contains optimal solutions to its subproblems.
3. **Sorting-Based Approach** - Many greedy problems benefit from sorting the input first.
4. **Non-Backtracking** - Once a choice is made, it is never reconsidered.

### **When to Use Greedy Algorithms?**
Greedy algorithms are ideal for:
- Optimization problems where a local choice leads to the global optimal solution.
- Problems that require minimizing or maximizing some property (e.g., minimizing conflicts, maximizing value).
- Problems where we can sort the input to facilitate decision-making.

Common greedy problems include **Huffman coding, Prim's and Kruskal’s algorithms (for MST), Dijkstra’s shortest path, Activity selection, and Interval scheduling**.

---

## **1. Fractional Knapsack**

### **Problem Statement**
Given `n` items with their corresponding weights and values, and a knapsack with a maximum weight capacity `W`, the goal is to maximize the total value by selecting items. Unlike the **0/1 Knapsack problem**, we can take fractional parts of items.

### **Approach: Greedy Strategy (O(n log n))**
The greedy strategy involves:
1. Calculating the **value-to-weight ratio** for each item.
2. Sorting the items in **descending order** based on this ratio.
3. Picking items greedily until the knapsack is full.

### **Code:**
```python
from typing import List, Tuple

def fractional_knapsack(items: List[Tuple[int, int]], capacity: int) -> float:
    """
    Solves the Fractional Knapsack problem using a greedy approach.
    
    Args:
        items (list): List of tuples where each tuple (value, weight).
        capacity (int): Maximum weight the knapsack can hold.
    
    Returns:
        float: Maximum total value possible.
    """
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item[0] / item[1], reverse=True)
    
    total_value = 0.0
    
    for value, weight in items:
        if capacity >= weight:
            # Take the full item
            capacity -= weight
            total_value += value
        else:
            # Take the fraction of the item
            total_value += (value / weight) * capacity
            break
    
    return total_value
```

---

## **2. Non-overlapping Intervals**

### **Problem Statement**
Given a set of intervals `[start, end]`, determine the **minimum number of intervals** that need to be removed to make the remaining intervals non-overlapping.

### **Approach: Greedy Strategy (O(n log n))**
1. **Sort** the intervals by **ending time**.
2. Iterate through intervals and greedily pick non-overlapping ones.
3. Count the removed intervals.

### **Code:**
```python
from typing import List

def non_overlapping_intervals(intervals: List[List[int]]) -> int:
    """
    Finds the minimum number of intervals to remove to eliminate overlaps.
    
    Args:
        intervals (list): List of intervals [start, end].
    
    Returns:
        int: Minimum number of intervals to remove.
    """
    if not intervals:
        return 0
    
    # Sort by ending times
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    prev_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            # Overlapping interval, remove it
            count += 1
        else:
            # Update previous end time
            prev_end = intervals[i][1]
    
    return count
```

---

## **Advantages & Disadvantages of Greedy Algorithms**

### **Advantages:**
✔ Fast and efficient (often O(n log n) complexity due to sorting).
✔ Simple to implement.
✔ Works well for many real-world problems (e.g., Huffman coding, Dijkstra’s algorithm).

### **Disadvantages:**
✖ Does not always provide the globally optimal solution.
✖ Cannot be used when future decisions depend on earlier ones.
✖ May require additional proof to confirm correctness.

---

## **Conclusion**

Today, we explored two fundamental greedy problems:
1. **Fractional Knapsack** - Using a greedy approach to maximize value.
2. **Non-overlapping Intervals** - Using sorting and a greedy method to minimize removals.

Greedy algorithms are efficient and widely used in optimization problems. Keep practicing, and see you tomorrow!