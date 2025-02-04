# **Day 31: Sorting**

Welcome to Day 31 of **50 Days of DSA in Python**! Today, we dive deeper into sorting algorithms with **Selection Sort** and **Merge Sort**. These algorithms are more efficient than the basic sorting algorithms we covered earlier and are essential for mastering sorting techniques.

---

### **Topics Covered:**
- Sorting  
- Selection Sort  
- Merge Sort  

---

## **1. Selection Sort**

### **Problem Statement**  
Selection Sort is a comparison-based sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first unsorted element. This process continues until the entire list is sorted.

### **Approach**

#### **1. Selection Sort Algorithm**

In each pass, the algorithm selects the smallest (or largest) element from the unsorted part of the list and swaps it with the first unsorted element. This reduces the unsorted part by one in each iteration.

#### **Code:**
```python
def selectionSort(nums):
    """
    Sort the list using Selection Sort.

    Args:
        nums (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(nums)
    
    # Traverse through all elements in the list
    for i in range(n):
        min_idx = i
        
        # Find the minimum element in the unsorted part
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of unsorted part
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    
    return nums
```

---

## **2. Merge Sort**

### **Problem Statement**  
Merge Sort is a divide-and-conquer algorithm that breaks the array into smaller subarrays, sorts them, and then merges them back together to form a sorted array. It is much more efficient than Selection Sort and performs well even on large datasets.

### **Approach**

#### **1. Merge Sort Algorithm**

The algorithm works by dividing the array into two halves, recursively sorting each half, and then merging the sorted halves. The merging process ensures that the resulting array is sorted.

#### **Code:**
```python
def mergeSort(nums):
    """
    Sort the list using Merge Sort.

    Args:
        nums (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(nums) <= 1:
        return nums
    
    # Divide the array into two halves
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted lists into a single sorted list.

    Args:
        left (list): The left sorted list.
        right (list): The right sorted list.

    Returns:
        list: The merged sorted list.
    """
    sorted_list = []
    i = j = 0
    
    # Compare elements from both lists and add the smaller one to sorted_list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Append remaining elements from both lists (if any)
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list
```

---

### **Conclusion**

Today, we explored two different sorting algorithms:

1. **Selection Sort**: A comparison-based sorting algorithm that selects the minimum (or maximum) element from the unsorted part and swaps it with the first unsorted element. It is simple to understand but inefficient for large datasets due to its O(n²) time complexity.
   
2. **Merge Sort**: A more efficient divide-and-conquer sorting algorithm with O(n log n) time complexity. It recursively divides the list into two halves, sorts them, and then merges them to produce a sorted list. Merge Sort is much faster than Selection Sort and is ideal for larger datasets.

While Selection Sort has its use cases, Merge Sort is generally preferred for larger lists due to its better time complexity. Keep practicing and experimenting with these algorithms to solidify your understanding.

See you tomorrow for more DSA adventures!