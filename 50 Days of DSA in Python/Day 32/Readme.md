# **Day 32: Sorting**

Welcome to Day 32 of **50 Days of DSA in Python**! Today, we cover two more important sorting algorithms: **Quick Sort** and **Radix Sort**. These algorithms are highly efficient in various scenarios and are widely used in practice for sorting large datasets.

---

### **Topics Covered:**
- Sorting  
- Quick Sort  
- Radix Sort  

---

## **1. Quick Sort**

### **Problem Statement**  
Quick Sort is a divide-and-conquer algorithm that works by selecting a pivot element and partitioning the array around it. Elements smaller than the pivot go to the left, and elements greater than the pivot go to the right. The process is then recursively applied to the left and right subarrays until the entire array is sorted.

### **Approach**

#### **1. Quick Sort Algorithm**

Quick Sort selects a pivot element, partitions the array, and recursively sorts the two halves. The key operation is partitioning the array such that all elements smaller than the pivot are on one side and all elements greater are on the other.

#### **Code:**
```python
def quickSort(nums):
    """
    Sort the list using Quick Sort.

    Args:
        nums (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(nums) <= 1:
        return nums

    # Select the pivot (last element in the array)
    pivot = nums[-1]
    left = []
    right = []
    
    # Partition the list into left (smaller than pivot) and right (greater than pivot)
    for num in nums[:-1]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    
    # Recursively apply quickSort to the left and right subarrays
    return quickSort(left) + [pivot] + quickSort(right)
```

---

## **2. Radix Sort**

### **Problem Statement**  
Radix Sort is a non-comparative sorting algorithm that sorts numbers based on individual digits. It processes each digit of the number starting from the least significant digit (LSD) to the most significant digit (MSD). Radix Sort is most efficient when dealing with integers or strings and is often used in applications where comparisons of large numbers are inefficient.

### **Approach**

#### **1. Radix Sort Algorithm**

Radix Sort processes numbers digit by digit, starting from the least significant digit. It groups the numbers based on each digit, using a stable sorting algorithm (like Counting Sort) for each pass. The process continues until all digits have been processed.

#### **Code:**
```python
def radixSort(nums):
    """
    Sort the list using Radix Sort.

    Args:
        nums (list): The list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(nums) == 0:
        return nums

    # Find the maximum number to know the number of digits
    max_num = max(nums)
    place = 1  # Start with the least significant digit
    
    while max_num // place > 0:
        nums = countingSortByDigit(nums, place)
        place *= 10

    return nums

def countingSortByDigit(nums, place):
    """
    Perform Counting Sort based on the digit represented by 'place'.

    Args:
        nums (list): The list of integers to be sorted.
        place (int): The digit place (1 for ones, 10 for tens, etc.).

    Returns:
        list: The list sorted by the digit at 'place'.
    """
    output = [0] * len(nums)
    count = [0] * 10

    # Store count of occurrences in count[]
    for num in nums:
        index = num // place % 10
        count[index] += 1

    # Change count[i] so that count[i] now contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output list
    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        index = num // place % 10
        output[count[index] - 1] = num
        count[index] -= 1

    return output
```

---

### **Conclusion**

Today, we covered two advanced sorting algorithms:

1. **Quick Sort**: A highly efficient divide-and-conquer sorting algorithm that selects a pivot, partitions the array around it, and recursively sorts the two halves. It has an average time complexity of O(n log n), making it one of the fastest sorting algorithms in practice.

2. **Radix Sort**: A non-comparative sorting algorithm that sorts numbers digit by digit, using a stable sorting algorithm for each pass. Radix Sort is very efficient when sorting large datasets of integers or strings and can achieve a time complexity of O(nk), where **n** is the number of elements and **k** is the number of digits.

Both algorithms are essential for efficiently handling large datasets, and mastering them will give you a strong understanding of sorting techniques.

Keep practicing and see you tomorrow for more exciting algorithms!