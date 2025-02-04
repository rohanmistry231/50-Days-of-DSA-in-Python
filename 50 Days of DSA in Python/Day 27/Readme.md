# **Day 27: Strings**

Welcome to Day 27 of **50 Days of DSA in Python**! Today, we dive deeper into **Strings**, focusing on two interesting problems: **Longest Unique Substring** and **Group Anagrams**.

---

### **Topics Covered:**
- Strings  
- Longest Unique Substring  
- Group Anagrams  

---

## **1. Longest Unique Substring**

### **Problem Statement**  
Given a string `s`, find the length of the longest substring that contains **no repeating characters**.

### **Approaches**

#### **1. Using Sliding Window (Optimal Approach)**

We can use the sliding window technique to maintain a window of characters that doesn't contain any duplicates. We expand the window by moving the right pointer, and if a duplicate character is found, we move the left pointer to remove the duplicate.

#### **Code:**
```python
def lengthOfLongestSubstring(s):
    """
    Find the length of the longest substring without repeating characters using sliding window.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring without repeating characters.
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

---

## **2. Group Anagrams**

### **Problem Statement**  
Given a list of strings, group the strings that are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word.

### **Approaches**

#### **1. Using Hash Map (Optimal Approach)**

We can use a hash map (dictionary) to group anagrams by sorting the characters in each string and using the sorted string as the key. Strings that are anagrams will have the same sorted key.

#### **Code:**
```python
def groupAnagrams(strs):
    """
    Group the anagrams in the given list of strings.

    Args:
        strs (list): A list of strings.

    Returns:
        list: A list of lists containing grouped anagrams.
    """
    anagrams = {}

    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        anagrams[sorted_str].append(s)

    return list(anagrams.values())
```

---

### **Conclusion**

Today, we worked on two important string manipulation problems:

1. **Longest Unique Substring**: We used the sliding window technique to find the longest substring without repeating characters.
2. **Group Anagrams**: We grouped strings that are anagrams using a hash map, with the sorted string as the key.

Both problems are common in string processing and provide a solid foundation for handling various real-world applications like text processing and pattern matching. Keep practicing, and see you tomorrow!