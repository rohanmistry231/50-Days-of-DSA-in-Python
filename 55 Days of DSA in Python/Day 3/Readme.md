```markdown
# Day 4: Backtracking and Problem Solving

Welcome to Day 4 of **55 Days of DSA in Python**! On this day, we delved into **Backtracking**, exploring its applications through two intriguing problems: **Permutations** and **Unique Permutations**. This README provides a comprehensive understanding of these topics, complete with their solutions.

---

## **Topics to be Covered**

- Backtracking  
- Permutations  
- Unique Permutations  

---

### **[Day 4](./Day%204):**

### Backtracking:

#### **What is Backtracking?**  
Backtracking is an algorithmic technique used to solve problems incrementally by building solutions piece by piece. At each step, it explores the solution space and abandons paths that do not satisfy the problem's constraints. Backtracking is especially useful in problems where we need to generate all possible configurations or make choices sequentially.

---

#### **How is Backtracking Different from Recursion?**  
Backtracking is often implemented using recursion, but they are not the same concept. Here's how they differ:  

| **Feature**              | **Recursion**                                                                 | **Backtracking**                                                                                           |
|---------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Definition**            | A function calling itself until a base condition is met.                     | A recursive approach combined with a strategy to revert changes and explore other possibilities.          |
| **Focus**                 | Solving a problem by breaking it into smaller subproblems.                   | Exploring all possible solutions and rejecting invalid ones dynamically.                                  |
| **State Management**      | Does not necessarily revert changes made in recursive calls.                 | Explicitly undoes changes (backtracks) after a path is explored to restore the previous state.            |
| **Applications**          | Solving problems like Fibonacci sequence, factorial, etc.                   | Problems like permutations, combinations, Sudoku solver, N-Queens, and constraint satisfaction problems. |

---

#### **How Does Backtracking Work?**  
Backtracking works by using a **decision tree** to explore all potential solutions for a problem. It involves the following steps:  

1. **Choose**: Make a choice from the available options.  
2. **Explore**: Proceed with the chosen option recursively.  
3. **Backtrack**: If the current path leads to a dead end (violates constraints), undo the last choice and try another.  

**Example Workflow**:  
For a permutation problem with input `[1, 2, 3]`:  
- Start with `1` → Explore permutations starting with `1`.  
- Add `2` to `1` → Explore permutations of `[1, 2]`.  
- Add `3` to `[1, 2]` → `[1, 2, 3]` is a valid permutation.  
- Backtrack by removing `3` → Explore other numbers at the last position.  

---

#### **Pass by Reference / Change Inplace**  
In backtracking, it is common to modify data structures like arrays or lists "inplace" (directly modifying the original data).  
- **Pass by Reference**: The same object is used and modified across recursive calls.  
- **Undo Changes**: After exploring one option, the changes are reverted to their previous state.  

Example of inplace modification in Python:  
```python
nums[i], nums[j] = nums[j], nums[i]  # Swap to explore
# Perform recursive exploration
nums[i], nums[j] = nums[j], nums[i]  # Undo swap (backtrack)
```

This minimizes memory usage as no additional copies are created.

---

#### **Blueprint to Solve Questions Using Backtracking**  
Here’s a systematic approach to solve backtracking problems:

1. **Understand the Problem**:
   - What are the constraints?
   - What is the goal (e.g., generate permutations, combinations, solve a grid)?
   
2. **Define the State**:
   - What represents a partial solution?
   - For permutations, the state is the current arrangement of elements.

3. **Identify Choices**:
   - What are the valid options at each step?
   - For combinations, choices are unselected elements.

4. **Write the Recursive Function**:
   - Include base and recursive cases.
   - Use a loop to iterate through choices.

5. **Backtrack**:
   - Revert the state after exploring a path.

---

#### **Identify When to Use Backtracking**  
Backtracking is useful in problems with the following characteristics:  
1. **Exhaustive Search**: The problem requires generating all configurations.  
2. **Constraints**: Solutions must satisfy specific conditions (e.g., Sudoku).  
3. **Optimization**: Searching for optimal configurations under constraints.  

---

### Updated Code: Permutations (With Comments and Enhanced Understanding)  

```python
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations of a list of numbers using backtracking.

    Args:
        nums (List[int]): A list of integers to permute.

    Returns:
        List[List[int]]: A list containing all permutations of the input list.
    """
    res = []  # List to store all permutations
    n = len(nums)  # Length of the input list

    def backtrack(start: int):
        """
        Backtracking function to generate permutations.

        Args:
            start (int): Current index for permutation generation.
        """
        # Base Case: If we've reached the last index, add the permutation
        if start == n:
            res.append(nums[:])  # Append a copy of nums to results
            return

        # Iterate through the possible choices
        for i in range(start, n):
            # Swap the current index with the choice index
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)  # Recurse to the next index
            nums[start], nums[i] = nums[i], nums[start]  # Backtrack (undo the swap)

    backtrack(0)  # Start the recursion from the first index
    return res
```

---

### Updated Code: Unique Permutations  

```python
from typing import List

def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations of a list of numbers using backtracking.

    Args:
        nums (List[int]): A list of integers that might contain duplicates.

    Returns:
        List[List[int]]: A list containing all unique permutations of the input list.
    """
    res = []  # List to store all unique permutations

    def backtrack(start: int):
        """
        Backtracking function to generate unique permutations.

        Args:
            start (int): Current index for permutation generation.
        """
        if start == len(nums):
            res.append(nums[:])  # Append a copy of nums to results
            return

        seen = set()  # Set to track processed elements at the current recursion level
        for i in range(start, len(nums)):
            if nums[i] not in seen:  # Skip duplicate elements
                seen.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]  # Swap elements
                backtrack(start + 1)  # Recurse for the next index
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack

    nums.sort()  # Sort the input to group duplicates
    backtrack(0)  # Start the recursion from the first index
    return res
```  

---

#### Permutations
**Problem**: Generate all permutations of a list of distinct integers.

**Recursive Solution**:
The recursive solution involves swapping elements to explore all possible arrangements of the list. The base case is reached when all positions are fixed, at which point the current permutation is added to the result.

**Python Implementation**:
```python
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations of a list of numbers.

    Args:
        nums (List[int]): A list of integers to permute.

    Returns:
        List[List[int]]: A list containing all permutations of the input list.
    """
    res = []  # List to store all permutations
    n = len(nums)  # Length of the input list

    def helper(i: int):
        """
        Recursive helper function to generate permutations.

        Args:
            i (int): Current index for permutation generation.
        """
        if i == n - 1:
            res.append(nums[:])  # Append a copy of nums to results
            return

        for j in range(i, n):
            nums[i], nums[j] = nums[j], nums[i]  # Swap elements
            helper(i + 1)  # Recurse for the next index
            nums[i], nums[j] = nums[j], nums[i]  # Backtrack (undo the swap)

    helper(0)  # Start the recursion from the first index
    return res
```

**Complexity**:
- Time Complexity: \( O(n \times n!) \), where \( n \) is the length of the list.
- Space Complexity: \( O(n) \), for the recursion stack.

---

#### Unique Permutations
**Problem**: Generate all unique permutations of a list of integers, which may contain duplicates.

**Recursive Solution**:
The recursive solution builds upon the permutations approach, with additional logic to handle duplicates. By using a set to track processed elements at each recursion level, we avoid generating duplicate permutations.

**Python Implementation**:
```python
from typing import List

def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations of a list of numbers, including duplicates.

    Args:
        nums (List[int]): A list of integers that might contain duplicates.

    Returns:
        List[List[int]]: A list containing all unique permutations of the input list.
    """
    res = []  # List to store all unique permutations

    def helper(index: int):
        """
        Recursive helper function to generate unique permutations.

        Args:
            index (int): Current index for permutation generation.
        """
        if index == len(nums) - 1:
            res.append(nums[:])  # Append a copy of nums to results
            return

        seen = set()  # Set to track processed elements
        for j in range(index, len(nums)):
            if nums[j] not in seen:  # Skip duplicates
                seen.add(nums[j])
                nums[index], nums[j] = nums[j], nums[index]  # Swap elements
                helper(index + 1)  # Recurse for the next index
                nums[index], nums[j] = nums[j], nums[index]  # Backtrack (undo the swap)

    nums.sort()  # Sort the input to ensure duplicates are grouped
    helper(0)  # Start the recursion from the first index
    return res
```

**Complexity**:
- Time Complexity: \( O(n \times n!) \), with deduplication reducing total permutations.
- Space Complexity: \( O(n) \), for the recursion stack.

---

#### Conclusion
Day 4 provided insights into:
1. **Backtracking**: A powerful technique for exploring all possibilities while pruning invalid paths.
2. **Permutations**: Solving for all arrangements of distinct elements.
3. **Unique Permutations**: Addressing duplicates to generate only distinct arrangements.