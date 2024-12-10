# Day 5: Backtracking and Subsets

Welcome to Day 5 of **55 Days of DSA in Python**! Today, we dive deeper into **Backtracking**, a powerful problem-solving technique, and focus on its application in solving **Subsets Problems**. This README will guide you through the concepts, code, and detailed analysis of the problems tackled on this day.

---

## **Topics to be Covered**

- Backtracking  
- Subsets

---

### **[Day 5](./Day%205):**

#### **1. Backtracking**
Backtracking is a problem-solving technique used to explore all potential solutions to a problem by incrementally building candidates and abandoning those that fail to meet the problem's constraints. It is particularly useful in solving combinatorial problems like generating subsets, permutations, and combinations.

##### **Backtracking in the Context of Subsets**
When generating subsets of a given list, backtracking is used to explore all combinations of including or excluding each element. The decision to include an element is made at each step, with the algorithm recursively exploring all possible subsets. The solution space is systematically traversed, ensuring that every subset is generated exactly once.

**Steps in Backtracking for Subsets:**
1. **Include the Current Element**: Add the current element to the subset.
2. **Exclude the Current Element**: Skip the current element and move to the next.
3. **Base Case**: Stop the recursion when all elements have been processed.
4. **Backtrack**: Undo the inclusion or exclusion of the last element to explore the next possibility.

Key points to remember:
- Subsets are generated in \( O(2^n) \) time due to the two decisions (include or exclude) for each element.
- Backtracking leverages recursion and systematically explores the solution space.

---

#### **2. Subsets**

The subsets problem focuses on generating all possible subsets (or the power set) of a given list of integers. These problems demonstrate the elegance and power of backtracking in solving combinatorial problems.

---

### Problem 1: **Generate All Subsets**

##### **Problem Statement**
Generate all subsets (the power set) of a given list of integers using backtracking.

##### **Solution**
The approach uses backtracking to include or exclude each element and systematically generates all subsets.

Here is the Python implementation:

```python
from typing import List

def generate_power_set(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets (power set) of a given list using backtracking.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        List[List[int]]: A list containing all subsets of the input list.

    Time Complexity:
        O(2^n): Each element can be included or excluded, resulting in 2^n subsets.

    Space Complexity:
        O(n): The recursion stack can go as deep as the number of elements in the list.
    """
    subsets = []

    def backtrack(index: int, current_subset: List[int]):
        """
        Backtracking helper function to generate subsets.

        Args:
            index (int): The current index in the list being processed.
            current_subset (List[int]): The current subset being constructed.
        """
        # Base Case: Add the constructed subset when all elements are processed
        if index == len(nums):
            subsets.append(current_subset[:])
            return

        # Include the current element
        current_subset.append(nums[index])
        backtrack(index + 1, current_subset)

        # Exclude the current element
        current_subset.pop()
        backtrack(index + 1, current_subset)

    backtrack(0, [])
    return subsets
```

---

### Problem 2: **Generate Unique Subsets with Duplicates**

##### **Problem Statement**
Given a list of integers that may contain duplicates, generate all unique subsets (power set) using backtracking.

##### **Solution**
The solution handles duplicates by sorting the input list and skipping duplicate elements during backtracking.

Here is the Python implementation:

```python
from typing import List

def subsets_with_duplicates(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets (the power set) of a given list with handling for duplicates using backtracking.

    Args:
        nums (List[int]): A list of integers, which may include duplicates.

    Returns:
        List[List[int]]: A list containing all unique subsets of the input list.

    Time Complexity:
        O(2^n): Each element can either be included or excluded, resulting in 2^n subsets.
        Sorting the input adds an additional O(n log n) complexity.

    Space Complexity:
        O(n): The recursion stack can go as deep as the number of elements in the list.
    """
    result = []
    nums.sort()

    def backtrack(index: int, current_subset: List[int]):
        """
        Backtracking helper function to generate subsets.

        Args:
            index (int): The current index in the list being processed.
            current_subset (List[int]): The current subset being constructed.
        """
        # Base Case: If all elements have been considered
        if index == len(nums):
            result.append(current_subset[:])  # Append a copy of the current subset
            return

        # Include the current element
        current_subset.append(nums[index])
        backtrack(index + 1, current_subset)
        current_subset.pop()

        # Exclude the current element and skip duplicates
        while index < len(nums) - 1 and nums[index] == nums[index + 1]:
            index += 1
        backtrack(index + 1, current_subset)

    # Initialize the recursion with an empty subset
    backtrack(0, [])
    return result
```

---

### **Conclusion**

Day 5 provided insights into:
1. **Backtracking**: Its role in systematically exploring solution spaces for combinatorial problems like subsets.
2. **Subsets Problems**:
    - **Generate All Subsets**: Understanding the basic approach to generating power sets using backtracking.
    - **Unique Subsets with Duplicates**: Learning to handle duplicate elements while generating subsets.