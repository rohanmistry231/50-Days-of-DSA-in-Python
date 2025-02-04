# **Day 26: Strings**

Welcome to Day 26 of **50 Days of DSA in Python**! Today, we focus on **Strings**, one of the most fundamental data structures. We will cover two interesting problems: **Non-Repeating Character** and **Palindrome**.

---

### **Topics Covered:**
- Strings  
- Non-Repeating Character  
- Palindrome  

---

## **1. Non-Repeating Character**

### **Problem Statement**  
Given a string `s`, find the first non-repeating character in it. If there is no non-repeating character, return `None`.

### **Approaches**

#### **1. Using Hash Table (Optimal Approach)**

We can use a hash table (dictionary in Python) to store the frequency of each character in the string. Once we have the frequencies, we can iterate through the string again to find the first character with a frequency of 1.

#### **Code:**
```python
def firstUniqChar(s):
    """
    Find the first non-repeating character in the string using a hash table.

    Args:
        s (str): The input string.

    Returns:
        int: The index of the first non-repeating character, or -1 if none exists.
    """
    freq = {}
    
    # Count the frequency of each character
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find the first character with frequency 1
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    
    return -1
```

---

## **2. Palindrome**

### **Problem Statement**  
Given a string `s`, determine if it is a **palindrome**. A palindrome is a word, phrase, or sequence that reads the same backward as forward, ignoring spaces, punctuation, and capitalization.

### **Approaches**

#### **1. Using Two Pointers (Optimal Approach)**

We can use two pointers, one starting at the beginning of the string and the other at the end. We compare the characters at these two positions and move the pointers towards each other. If the characters don't match, we return `False`. If we reach the middle without finding any mismatches, we return `True`.

#### **Code:**
```python
def isPalindrome(s):
    """
    Check if the string is a palindrome using two pointers.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, otherwise False.
    """
    s = ''.join(char.lower() for char in s if char.isalnum())  # Remove non-alphanumeric characters and lowercase
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```

---

### **Conclusion**

Today, we focused on **Strings** and covered two classic problems:

1. **Non-Repeating Character**: We used a hash table to efficiently find the first non-repeating character in the string.
2. **Palindrome**: We solved the palindrome check problem using two pointers, ignoring non-alphanumeric characters and case.

Strings are integral to solving many algorithmic challenges, and these problems showcase how to handle common string manipulations. Keep practicing, and see you tomorrow!