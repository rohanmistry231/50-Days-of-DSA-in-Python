# Day 6: Backtracking and Combinations

Welcome to Day 6 of **55 Days of DSA in Python**! Today, we continue exploring **Backtracking**, focusing on its application in solving **Combinations** and **Combination Sum Problems**. This README will guide you through the concepts, code, and detailed analysis of the problems tackled on this day.

---

## **Topics Covered**
### **[Day 6](./Day%206):**
- Backtracking  
- Combinations  
- Combination Sum 1  

---

## **Backtracking in the Context of Combinations**

Backtracking is a powerful algorithmic technique used to solve combinatorial problems. It systematically explores all possible solutions by building candidates incrementally and abandoning them ("backtracking") as soon as it determines that the current path will not lead to a valid solution.

### **How Backtracking Works for Combinations**
1. **Recursive Exploration**: Backtracking involves recursively adding elements to the current solution.
2. **Base Case**: If the combination reaches the desired length or meets the target condition, it is added to the result.
3. **Pruning**: Optimizations can be added to reduce the search space, such as skipping duplicate elements or avoiding unnecessary iterations.

Backtracking is particularly useful for generating combinations, as it allows us to efficiently explore the search space without missing any possibilities.

---

### **Combinations**

Combinations are a fundamental concept in combinatorics, where we aim to select a subset of items from a given set, without considering the order of selection. In this section, we explore how **Backtracking** is used to generate combinations.

---

#### **Problem 1: Generate Combinations (Normal Approach)**

This problem involves generating all possible combinations of `k` numbers chosen from the range `[1, n]`. We use a backtracking approach to explore the solution space efficiently.

```python
from typing import List

def generate_combinations(n: int, k: int) -> List[List[int]]:
    """
    Generate all possible combinations of k numbers chosen from the range [1, n].

    Args:
        n (int): The upper limit of the range (inclusive).
        k (int): The size of each combination.

    Returns:
        List[List[int]]: A list containing all possible combinations.

    Time Complexity:
        O(C(n, k)): The number of combinations is n! / (k! * (n - k)!).
        Each combination requires O(k) time to copy to the result.

    Space Complexity:
        O(k): The recursion stack can go as deep as the size of each combination.

    Example:
        Input: n = 4, k = 2
        Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """
    combinations = []

    def backtrack(start: int, current_combination: List[int]) -> None:
        """
        Helper function to generate combinations using backtracking.

        Args:
            start (int): The starting number for the current recursion.
            current_combination (List[int]): The combination being built.
        """
        # Base Case: If the current combination has k numbers, add it to the result
        if len(current_combination) == k:
            combinations.append(current_combination[:])  # Add a copy of the current combination
            return

        # Explore further by adding numbers to the combination
        for number in range(start, n + 1):
            # Include the current number
            current_combination.append(number)
            backtrack(number + 1, current_combination)

            # Exclude the current number (backtrack)
            current_combination.pop()

    # Start backtracking with an empty combination
    backtrack(1, [])
    return combinations
```

#### **Problem 2: Combinations with Optimization**

In this version, we optimize the approach by reducing the range of iteration based on how many numbers are still required to complete a combination. This minimizes unnecessary recursive calls, making the algorithm more efficient.

```python
from typing import List

def find_combinations_optimized(n: int, k: int) -> List[List[int]]:
    """
    Find all unique combinations of k numbers from the range [1, n].

    Optimized by reducing the range of iteration based on the remaining elements needed.

    Args:
        n (int): The upper limit of the range (inclusive).
        k (int): The size of each combination.

    Returns:
        List[List[int]]: A list of all unique combinations.

    Time Complexity:
        O(C(n, k)): The time complexity corresponds to the number of combinations, which is n! / (k! * (n-k)!).

    Space Complexity:
        O(k): The maximum depth of the recursion stack.

    Example:
        Input: n = 4, k = 2
        Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """
    combinations = []

    def backtrack(start: int, current_combination: List[int]) -> None:
        """
        Helper function to generate combinations using backtracking.

        Args:
            start (int): The starting index for the current recursion.
            current_combination (List[int]): The current combination being built.
        """
        # If the current combination has the required size, save it
        if len(current_combination) == k:
            combinations.append(current_combination[:])  # Add a copy of the current combination
            return

        # Calculate the number of elements still needed
        need = k - len(current_combination)

        # Iterate over the range with an optimized end to reduce unnecessary recursion
        for i in range(start, n - (need - 1) + 1):
            # Include the current number
            current_combination.append(i)
            backtrack(i + 1, current_combination)

            # Exclude the current number (backtrack)
            current_combination.pop()

    # Start backtracking with an empty combination
    backtrack(1, [])
    return combinations
```
---

## **Combination Sum 1**

### **Problem: Find All Unique Combinations That Sum to a Target**
Given an array of distinct integers `candidates` and a target integer `target`, return all unique combinations of `candidates` where the chosen numbers sum to `target`. You may reuse elements of `candidates` as many times as necessary.

**Solution**
```python
from typing import List

def find_combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations of numbers that sum to a target.

    Args:
        candidates (List[int]): List of candidate numbers.
        target (int): Target sum.

    Returns:
        List[List[int]]: A list of all unique combinations.

    Time Complexity:
        O(2^n): Each number has two choices (include or exclude), leading to an exponential time complexity.
    
    Space Complexity:
        O(target): Maximum depth of recursion corresponds to the target sum.

    Example:
        Input: candidates = [2, 3, 6, 7], target = 7
        Output: [[2, 2, 3], [7]]
    """
    result = []

    def backtrack(index: int, current_combination: List[int], current_sum: int) -> None:
        if current_sum > target:
            return
        if current_sum == target:
            result.append(current_combination[:])
            return
        for i in range(index, len(candidates)):
            current_combination.append(candidates[i])
            backtrack(i, current_combination, current_sum + candidates[i])
            current_combination.pop()

    backtrack(0, [], 0)
    return result

if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target_value = 7
    result = find_combination_sum(candidates, target_value)
    print(f"All combinations of {candidates} that sum to {target_value} are:")
    for combination in result:
        print(combination)
```

---

## **Conclusion**
- **Backtracking**: An effective technique to explore the solution space systematically for combinatorial problems.
- **Combinations**:
  - First problem generates all combinations of a given size.
  - Optimized version reduces unnecessary iterations.
- **Combination Sum**:
  - Explores all unique ways to sum up to a target using candidate numbers.