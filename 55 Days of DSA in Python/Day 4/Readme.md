# Day 4: Backtracking and Permutation Problems

Welcome to Day 4 of **55 Days of DSA in Python**! On this day, we delved into **Backtracking**, a powerful algorithmic technique used to solve many optimization and combinatorial problems. We explored two major problems: **Permutations** and **Unique Permutations**, both solved using backtracking.

---

## **Topics to be Covered**

- Backtracking
- Permutations
- Unique Permutations

---

### **[Day 4](./Day%204):**

### **1. Backtracking**

#### **What is Backtracking?**

Backtracking is a general algorithm for finding all (or some) solutions to a computational problem, especially constraint satisfaction problems. It incrementally builds candidates for the solutions and abandons (backtracks) a candidate as soon as it is determined that it cannot be extended to a valid solution.

**Key Characteristics of Backtracking:**
- **Incremental Construction**: Backtracking builds solutions step-by-step and abandons partial solutions as soon as they are determined to be invalid.
- **Depth-First Search (DFS)**: Backtracking can be seen as a DFS algorithm where we explore each potential solution and "backtrack" to try a different option once we hit a dead end.
- **Efficiency**: It's an efficient method for solving problems where we need to explore all possibilities, such as puzzles, combinations, or permutations, but is slower than other algorithms for larger problem sizes due to its brute-force nature.

#### **How is Backtracking Different from Recursion?**

While recursion involves a function calling itself to break down a problem into smaller subproblems, **backtracking** is a type of recursion where we try different possible solutions and "backtrack" when a solution turns out to be invalid.

**Key Differences:**
- **Recursion**: Simply breaks the problem into smaller subproblems without necessarily pruning invalid paths.
- **Backtracking**: A refined approach, which prunes paths that are invalid or suboptimal as soon as they are detected.

#### **How Does Backtracking Work?**

Backtracking works by:
1. **Making a choice**: At each step, choose one option from the set of possible choices.
2. **Recursion**: Recursively explore the consequences of that choice.
3. **Backtrack**: If the current choice leads to an invalid solution or dead end, backtrack and try another choice.

**Pass by Reference / Change Inplace**: In many backtracking problems, we change the state of the solution space "in place" (i.e., by modifying the data structure directly) and backtrack by undoing the changes.

#### **Blueprint to Solve Questions Using Backtracking**

1. **Identify the decision space**: What are the options available at each step?
2. **Make a decision**: Choose an option and explore further.
3. **Recurse**: Dive deeper into the problem by solving subproblems.
4. **Backtrack**: Undo the choice if the current solution is invalid or not optimal.

#### **Identify / When to Use Backtracking?**

Backtracking is used when:
- The problem requires exploring all possible configurations.
- Constraints need to be satisfied at every step (e.g., Sudoku, N-Queens).
- There is a need for finding an optimal solution from a set of possibilities.

Backtracking is particularly useful in solving problems related to:
- Puzzles and games (e.g., Sudoku, N-Queens)
- Combinatorial problems (e.g., generating subsets or permutations)
- Pathfinding problems (e.g., maze solving)

---

### **2. Permutations**

### **Problem: Permutations**

The problem of generating all permutations of a given list of integers asks us to find every possible arrangement of the elements in the list, ensuring that each permutation is unique. A permutation is simply an ordered arrangement of elements.

**Key Points:**
- If the input list has `n` distinct elements, the total number of permutations is `n!` (n factorial), which means `n × (n-1) × (n-2) × ... × 1` possible arrangements.
- **Backtracking** is an ideal approach for generating permutations because we can incrementally build each permutation by swapping elements in place and then backtrack (undo the swap) to explore other potential arrangements.

**Code:**
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

### **3. Unique Permutations**

### **Problem: Unique Permutations**

In the case where the list might contain duplicate elements, we need to generate **unique permutations** only, meaning no duplicate arrangements. For example, given the list `[1, 1, 2]`, the possible permutations should be `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]` and not `[1, 1, 2]` twice.

**Key Points:**
- To handle duplicates, we need to make sure that we don’t generate the same permutation more than once. This can be achieved by skipping elements that have already been used in the current recursion level.
- **Sorting the input** list initially helps because duplicate numbers will be adjacent to each other, making it easier to skip them.

**Code:**
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

### **Why Sorting is Important?**

Sorting the list at the beginning ensures that duplicate elements are adjacent to each other, making it easy to detect and skip duplicates when generating permutations. Without sorting, it would be difficult to efficiently identify duplicate elements, and the algorithm would generate duplicate permutations.

---

### **Conclusion**

- **Permutations**: In the first problem, we generate all permutations by swapping elements and backtracking. This allows us to explore every possible arrangement.
- **Unique Permutations**: The second problem adds the complexity of handling duplicates. By sorting the list and skipping repeated elements at each recursion level, we ensure that only unique permutations are generated.