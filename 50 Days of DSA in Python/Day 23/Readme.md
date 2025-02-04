# **Day 23: Greedy Algorithms**

Welcome to Day 23 of **50 Days of DSA in Python**! Today, we continue our exploration of **Greedy Algorithms**, focusing on two classic problems: **Gas Stations** and **Jump Game 2**. Greedy algorithms are efficient solutions to optimization problems, where the goal is to make locally optimal choices at each step.

---

### **Topics Covered:**
- Greedy Algorithms  
- Gas Stations  
- Jump Game 2  

---

## **1. Gas Stations**

### **Problem Statement**  
Given an array of gas stations, each with a certain amount of gas, and an array of costs to travel to the next station, determine if there is a starting gas station such that you can travel around the circuit once without running out of gas. If such a station exists, return the starting index, otherwise, return -1.

### **Approaches**

#### **1. Greedy Approach**

The greedy approach involves checking whether we can complete a round starting from each station, ensuring that we accumulate enough gas to continue the journey.

#### **Code:**
```python
def canCompleteCircuit(gas, cost):
    """
    Determine if a trip around the circuit is possible starting from a gas station.

    Args:
        gas (list): A list of gas available at each station.
        cost (list): A list of gas required to reach the next station.

    Returns:
        int: The index of the starting station, or -1 if not possible.
    """
    total_gas = 0
    current_gas = 0
    start_index = 0

    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]

        # If the current gas is negative, reset the start index
        if current_gas < 0:
            start_index = i + 1
            current_gas = 0

    return start_index if total_gas >= 0 else -1
```

---

## **2. Jump Game 2**

### **Problem Statement**  
Given an array of non-negative integers `nums`, where each element represents your maximum jump length from that position, determine the minimum number of jumps to reach the last index.

### **Approaches**

#### **1. Greedy Approach**

The greedy approach involves calculating the farthest reachable index at each position and determining the minimum jumps required to reach the last index.

#### **Code:**
```python
def jump(nums):
    """
    Calculate the minimum number of jumps to reach the last index.

    Args:
        nums (list): A list of non-negative integers representing maximum jumps.

    Returns:
        int: The minimum number of jumps required to reach the last index.
    """
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                break

    return jumps
```

---

### **Conclusion**

Today, we explored two more problems that can be solved using **Greedy Algorithms**:

1. **Gas Stations**: Finding the starting station for a successful circuit journey using a greedy approach.
2. **Jump Game 2**: Determining the minimum number of jumps required to reach the last index using a greedy approach.

Greedy algorithms often provide optimal solutions for problems where local decisions lead to a globally optimal solution. Keep practicing, and see you tomorrow!