```markdown
### **[Day 4](./Day%204):**  

---

#### **1. Backtracking**  

---

##### **What is Backtracking?**  
Backtracking is a problem-solving technique used to build solutions incrementally, one piece at a time, and remove those solutions that fail to satisfy the constraints of the problem. It's often used for optimization problems or puzzles, such as finding paths in a maze, solving Sudoku, or generating permutations.  

##### **How is it Different from Recursion?**  
- **Recursion** is a general approach for solving problems by breaking them into smaller subproblems of the same type.  
- **Backtracking** is a specific form of recursion where we abandon a path or state once it is determined to be invalid.  

##### **How Does Backtracking Work?**  
1. Start from an initial state and attempt to move towards a solution.  
2. If the current path satisfies the constraints, move forward.  
3. If it violates constraints or doesn't lead to a solution, backtrack to the previous state and try a different path.  
4. Repeat the process until all possible paths are explored.  

##### **Pass by Reference / Change Inplace**  
In backtracking, passing by reference or changing elements in place is common to save memory and time. Modifications to the data structure are reverted during backtracking to maintain the original state.  

##### **Blueprint to Solve Questions Using Backtracking**  
1. Identify the decision point or choices to be made.  
2. Use recursion to explore each choice.  
3. Apply constraints or conditions to prune invalid solutions.  
4. Backtrack to undo changes when moving to the next choice.  

##### **Identify / When to Use Backtracking?**  
- Problems with multiple possible solutions requiring exploration of different combinations.  
- Constraints-based problems like Sudoku, N-Queens, and maze traversal.  

---

#### **2. Permutations**  

---

##### **Problem**: Generate all permutations of a list of numbers.  

##### **Code Solution**  
```python
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations of a list of numbers.

    Args:
        nums (List[int]): A list of integers to permute.

    Returns:
        List[List[int]]: A list containing all permutations of the input list.

    Time Complexity:
        The time complexity is O(n * n!), where n is the length of the input list.
        - There are n! permutations in total.
        - For each permutation, a copy of the list (O(n)) is appended to the result.
    """
    res = []  # List to store all the permutations
    n = len(nums)  # Length of the input list

    def helper(i: int):
        """
        Recursive helper function to generate permutations.

        Args:
            i (int): Current index for permutation generation.
        """
        # Base case: if the current index is the last one, add the current permutation
        if i == n - 1:
            res.append(nums[:])  # Append a copy of nums to results
            return

        # Recursive case: swap and generate permutations
        for j in range(i, n):
            nums[i], nums[j] = nums[j], nums[i]  # Swap elements at indices i and j
            helper(i + 1)  # Recurse for the next index
            nums[i], nums[j] = nums[j], nums[i]  # Backtrack (undo the swap)

    helper(0)  # Start the recursion from the first index
    return res

if __name__ == "__main__":
    # Example usage of the permute function
    numbers = [1, 2, 3]
    permutations = permute(numbers)
    print("Permutations of", numbers, "are:")
    for perm in permutations:
        print(perm)
```

---

#### **3. Permutations 2**  

---

##### **Problem**: Generate all unique permutations of a list of numbers, including duplicates.  

##### **Code Solution**  
```python
from typing import List

def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations of a list of numbers, including duplicates.

    Args:
        nums (List[int]): A list of integers that might contain duplicates.

    Returns:
        List[List[int]]: A list containing all unique permutations of the input list.

    Time Complexity:
        The time complexity is O(n * n!), where n is the length of the input list.
        - There are at most n! permutations.
        - However, duplicate elements reduce the number of unique permutations.
        - The function also uses a hash table for deduplication, which adds negligible overhead.
    """
    res = []  # List to store all unique permutations

    def permutations(index: int):
        """
        Recursive helper function to generate unique permutations.

        Args:
            index (int): Current index for permutation generation.
        """
        # Base case: if the current index is the last one, add the current permutation
        if index == len(nums) - 1:
            res.append(nums[:])  # Append a copy of nums to results
            return

        hash_set = {}  # Hash table to track duplicates in the current recursion
        for j in range(index, len(nums)):
            # Skip processing duplicate elements
            if nums[j] not in hash_set:
                hash_set[nums[j]] = True  # Mark the element as processed
                nums[index], nums[j] = nums[j], nums[index]  # Swap elements
                permutations(index + 1)  # Recurse for the next index
                nums[index], nums[j] = nums[j], nums[index]  # Backtrack (undo the swap)

    nums.sort()  # Sort the input to ensure duplicates are grouped
    permutations(0)  # Start the recursion from the first index
    return res

if __name__ == "__main__":
    # Example usage of the permute_unique function
    numbers = [1, 1, 2]
    unique_permutations = permute_unique(numbers)
    print("Unique permutations of", numbers, "are:")
    for perm in unique_permutations:
        print(perm)
```

---

#### **Conclusion**  
Day 4 covered **Backtracking**, a powerful technique for solving complex problems by exploring all possibilities with constraints. We implemented solutions for two permutation problems:
1. Generating all permutations of a list.
2. Generating unique permutations of a list with duplicates.