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

## **Combinations**

### **Problem 1: Generate All Combinations**
Find all combinations of size `k` from the numbers `1` to `n`.

**Optimized Solution**
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
        O(C(n, k)): The time complexity corresponds to the number of combinations, which is n! / (k! * (n-k)!)

    Space Complexity:
        O(k): The maximum depth of the recursion stack.

    Example:
        Input: n = 4, k = 2
        Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """
    combinations = []

    def backtrack(start: int, current_combination: List[int]) -> None:
        if len(current_combination) == k:
            combinations.append(current_combination[:])
            return

        need = k - len(current_combination)
        for i in range(start, n - (need - 1) + 1):
            current_combination.append(i)
            backtrack(i + 1, current_combination)
            current_combination.pop()

    backtrack(1, [])
    return combinations

if __name__ == "__main__":
    n_value = 4
    k_value = 2
    result = find_combinations_optimized(n_value, k_value)
    print(f"All {k_value}-combinations of numbers from 1 to {n_value} are:")
    for combination in result:
        print(combination)
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