# **Day 21: Greedy Algorithms - Two City Scheduling & Boats to Save People**

Welcome to Day 21 of **50 Days of DSA in Python**! Today, we continue our journey with **Greedy Algorithms**, focusing on two classic problems: **Two City Scheduling** and **Boats to Save People**. These problems emphasize optimal decision-making to minimize cost or maximize efficiency using a greedy approach.

---

### **Topics Covered:**
- Greedy Algorithms
- Two City Scheduling
- Boats to Save People

---

## **1. Two City Scheduling**

### **Problem Statement**
A company is planning to interview `2n` people in two different cities: City A and City B. The cost of sending the `i-th` person to City A is `costs[i][0]`, and the cost of sending them to City B is `costs[i][1]`. The goal is to send exactly `n` people to each city while minimizing the total cost.

### **Approach: Greedy Strategy (O(n log n))**
1. Calculate the **cost difference** between sending each person to City A vs. City B.
2. **Sort** the people based on this difference.
3. Send the first `n` people to **City A** (cheaper to A), and the remaining `n` people to **City B** (cheaper to B).

### **Code:**
```python
from typing import List

def two_city_scheduling(costs: List[List[int]]) -> int:
    """
    Minimizes the cost of sending people to two cities.
    
    Args:
        costs (list): List of [costA, costB] for each person.
    
    Returns:
        int: Minimum total cost.
    """
    # Sort by cost difference between City A and City B
    costs.sort(key=lambda x: x[0] - x[1])
    
    total_cost = 0
    n = len(costs) // 2
    
    # First n people go to City A, rest to City B
    for i in range(n):
        total_cost += costs[i][0]  # City A
    for i in range(n, 2 * n):
        total_cost += costs[i][1]  # City B
    
    return total_cost
```

---

## **2. Boats to Save People**

### **Problem Statement**
Given an array `people` where `people[i]` represents the weight of the `i-th` person and a boat has a maximum weight limit `limit`, find the **minimum number of boats** needed to carry every person. Each boat can carry at most **two people** at a time, provided their total weight does not exceed `limit`.

### **Approach: Greedy Two-Pointer Strategy (O(n log n))**
1. **Sort** the people by weight.
2. Use a **two-pointer technique**: one pointer at the lightest (`left`) and another at the heaviest (`right`).
3. If the sum of their weights is within the limit, board them together; otherwise, board the heavier person alone.
4. Move the pointers accordingly and count the boats.

### **Code:**
```python
from typing import List

def num_rescue_boats(people: List[int], limit: int) -> int:
    """
    Finds the minimum number of boats needed to save people.
    
    Args:
        people (list): List of people's weights.
        limit (int): Maximum weight a boat can carry.
    
    Returns:
        int: Minimum number of boats required.
    """
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # Take the lighter person as well
        right -= 1  # Always take the heavier person
        boats += 1
    
    return boats
```

---

### **Conclusion**

Today, we explored two fundamental problems in **Greedy Algorithms**:
1. **Two City Scheduling** - Used sorting and cost differences to optimize travel expenses.
2. **Boats to Save People** - Applied a two-pointer technique to efficiently assign people to boats.

Greedy algorithms help in solving optimization problems efficiently by making local optimal choices. Keep practicing, and see you tomorrow! 🚀