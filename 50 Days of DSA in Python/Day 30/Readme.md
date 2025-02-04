# **Day 30: Sorting**

Welcome to Day 30 of **50 Days of DSA in Python**! Today, we will focus on **Sorting Algorithms**, specifically **Bubble Sort** and **Insertion Sort**. These are fundamental sorting techniques, often used to understand the basic principles of sorting before moving to more advanced algorithms.

---

### **Topics Covered:**
- Sorting  
- Bubble Sort  
- Insertion Sort  

---

## **1. Bubble Sort**

### **Problem Statement**  
Bubble Sort is a simple comparison-based sorting algorithm that works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. The process is repeated until the list is sorted.

### **Approach**

#### **1. Bubble Sort Algorithm**

In each pass, the largest unsorted element "bubbles" up to its correct position. This continues for all elements until the entire list is sorted.

#### **Code:**
```python
def bubbleSort(nums):
    """
    Sort the list using Bubble Sort.

    Args:
        nums (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(nums)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to optimize: if no two elements were swapped in an inner loop, break early
        swapped = False
        
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        
        # If no two elements were swapped, the list is sorted
        if not swapped:
            break
            
    return nums
```

---

## **2. Insertion Sort**

### **Problem Statement**  
Insertion Sort is a simple sorting algorithm that builds the final sorted array one element at a time. It works much like sorting playing cards in your hands.

### **Approach**

#### **1. Insertion Sort Algorithm**

In this algorithm, we start with the second element and insert it in the correct position relative to the already sorted portion of the list. This continues until the entire list is sorted.

#### **Code:**
```python
def insertionSort(nums):
    """
    Sort the list using Insertion Sort.

    Args:
        nums (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        
        # Move elements of nums[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        
        nums[j + 1] = key
    
    return nums
```

---

### **Conclusion**

Today, we explored two basic but important sorting algorithms:

1. **Bubble Sort**: A simple comparison-based sorting algorithm, where the largest unsorted element "bubbles" to its correct position after each pass.
2. **Insertion Sort**: A sorting algorithm that builds the sorted array one element at a time by inserting elements into their correct position in the already sorted part of the array.

These algorithms provide a great foundation for understanding sorting. Although they are not the most efficient for large datasets, they are useful for small lists or partially sorted data. As we progress, we will explore more efficient sorting algorithms such as Quick Sort and Merge Sort.

Keep practicing, and see you tomorrow!