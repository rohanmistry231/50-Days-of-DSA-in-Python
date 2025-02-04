# **Day 25: Hash Tables**

Welcome to Day 25 of **50 Days of DSA in Python**! Today, we dive into **Hash Tables**, one of the most efficient data structures for solving various algorithmic challenges. We will cover two classic problems: **Two Sum** and **Isomorphic Strings**.

---

### **Topics Covered:**
- Hash Tables  
- Two Sum  
- Isomorphic Strings  

---

## **1. Two Sum**

### **Problem Statement**  
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

### **Approaches**

#### **1. Using Hash Table (Optimal Approach)**

We can use a hash table (dictionary in Python) to store the elements we've seen so far and their indices. For each element in the array, we check if the complement (i.e., `target - num`) exists in the hash table. This provides an efficient solution in `O(n)` time.

#### **Code:**
```python
def twoSum(nums, target):
    """
    Find two numbers in the list that add up to the target using a hash table.

    Args:
        nums (list): List of integers.
        target (int): The target sum.

    Returns:
        list: Indices of the two numbers.
    """
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
```

---

## **2. Isomorphic Strings**

### **Problem Statement**  
Given two strings `s` and `t`, determine if they are **isomorphic**. Two strings are isomorphic if the characters in `s` can be replaced to get `t`, with the condition that each character in `s` maps to exactly one character in `t`, and vice versa.

### **Approaches**

#### **1. Using Hash Tables (Optimal Approach)**

We can use two hash tables (or dictionaries) to track the character mappings between the two strings. For each character in the strings, we check if it already has a corresponding mapping. If not, we create a new mapping. If there's a conflict in mappings, we return `False`.

#### **Code:**
```python
def isIsomorphic(s, t):
    """
    Check if two strings are isomorphic using hash tables.

    Args:
        s (str): The first input string.
        t (str): The second input string.

    Returns:
        bool: True if the strings are isomorphic, otherwise False.
    """
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_map:
            if s_map[char_s] != char_t:
                return False
        else:
            s_map[char_s] = char_t

        if char_t in t_map:
            if t_map[char_t] != char_s:
                return False
        else:
            t_map[char_t] = char_s

    return True
```

---

### **Conclusion**

Today, we explored **Hash Tables** and how they can be used to efficiently solve problems:

1. **Two Sum**: We used a hash table to find two numbers that sum up to the target in `O(n)` time.
2. **Isomorphic Strings**: We used hash tables to check if two strings can be mapped onto each other, respecting character mappings.

Hash tables are powerful tools for many algorithmic problems, and these problems highlight how to leverage them for fast lookups and efficient solutions. Keep practicing, and see you tomorrow!