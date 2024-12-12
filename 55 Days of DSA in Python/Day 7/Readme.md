# Day 7: Backtracking and Advanced Combination Problems

Welcome to Day 7 of **55 Days of DSA in Python**! Today, we continue exploring **Backtracking**, focusing on advanced combination problems that build upon the foundational concepts of combinations and target sums. This README will guide you through the topics, concepts, and solutions covered on this day.

---

## **Topics Covered**
### **[Day 7](./Day%206):**
- Backtracking
- Combinations Sum 2
- Combination Sum 3

---

### **1. Backtracking in Combination Problems**

Backtracking is a systematic way to explore all possible configurations of a problem by building potential solutions incrementally and abandoning them ("backtracking") as soon as it becomes clear they cannot lead to a valid solution. In combination problems, backtracking helps us:

- Explore all subsets of a given list.
- Enforce constraints like specific sum targets or size limits.
- Avoid redundant computations by pruning invalid paths.

Today's problems involve finding combinations that meet specific criteria, such as:

1. Avoiding duplicate subsets (Combination Sum 2).
2. Limiting the size and range of numbers in each combination (Combination Sum 3).

---

## Problems and Solutions

### **2. Combination Sum 2**

In this problem, we aim to find unique combinations of numbers that sum to a given target. Each number in the input array may only be used once in the combination.

#### **Code**

```python
from typing import List

def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations of numbers in `candidates` that sum up to `target`.
    
    Args:
        candidates (List[int]): The list of numbers to choose from.
        target (int): The target sum for the combinations.

    Returns:
        List[List[int]]: A list of unique combinations that sum to the target.

    Time Complexity:
        O(2^n): In the worst case, we generate all subsets of the candidates.
    
    Space Complexity:
        O(n): For the recursion stack and current combination.

    Example:
        Input: candidates = [10,1,2,7,6,1,5], target = 8
        Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    """
    result = []
    candidates.sort()  # Sort to handle duplicates

    def backtrack(index: int, current_sum: int, current_combination: List[int]) -> None:
        """
        Recursive helper function to generate combinations using backtracking.

        Args:
            index (int): The starting index for the current recursion.
            current_sum (int): The sum of the current combination.
            current_combination (List[int]): The current combination being built.
        """
        if current_sum == target:
            result.append(current_combination[:])
            return

        if current_sum > target:
            return

        used = set()  # To track elements used at the current level

        for i in range(index, len(candidates)):
            if candidates[i] in used:
                continue  # Skip duplicates at the same level

            used.add(candidates[i])

            current_combination.append(candidates[i])
            backtrack(i + 1, current_sum + candidates[i], current_combination)
            current_combination.pop()

    backtrack(0, 0, [])
    return result

if __name__ == "__main__":
    input_candidates = [10, 1, 2, 7, 6, 1, 5]
    target_sum = 8
    output = combination_sum_2(input_candidates, target_sum)
    print(f"Unique combinations summing to {target_sum}: {output}")
```

---

### **2. Combination Sum 3**

In this problem, we find all valid combinations of `k` numbers that sum up to `n`, using only numbers from 1 to 9. Each number may only appear once in the combination.

#### **Code**

```python
from typing import List

def combination_sum_3(k: int, n: int) -> List[List[int]]:
    """
    Find all valid combinations of `k` numbers that sum up to `n`.
    Only numbers from 1 to 9 can be used, and each number may only appear once in the combination.

    Args:
        k (int): The number of numbers in each combination.
        n (int): The target sum for the combinations.

    Returns:
        List[List[int]]: A list of all valid combinations.

    Time Complexity:
        O(2^9): At most, we generate all subsets of the numbers from 1 to 9.

    Space Complexity:
        O(k): Space used for recursion stack and current combination.

    Example:
        Input: k = 3, n = 7
        Output: [[1, 2, 4]]
    """
    result = []

    def backtrack(start: int, current_combination: List[int], current_sum: int) -> None:
        """
        Recursive helper function to explore combinations using backtracking.

        Args:
            start (int): The starting number for the current recursion.
            current_combination (List[int]): The current combination being built.
            current_sum (int): The sum of the current combination.
        """
        if current_sum == n and len(current_combination) == k:
            result.append(current_combination[:])
            return

        if current_sum > n or len(current_combination) == k:
            return

        for number in range(start, 10):
            current_combination.append(number)
            backtrack(number + 1, current_combination, current_sum + number)
            current_combination.pop()

    backtrack(1, [], 0)
    return result

if __name__ == "__main__":
    k_value = 3
    target_sum = 7
    output = combination_sum_3(k_value, target_sum)
    print(f"Combinations of {k_value} numbers summing to {target_sum}: {output}")
```

---

## **Conclusion**  
- **Backtracking**: A systematic approach to explore possible solutions, especially useful for combinatorial problems.  
- **Combination Sum 2**:  
  - Finds unique combinations of candidates that sum to a target while ensuring no duplicate subsets by sorting and using hash maps for tracking.  
- **Combination Sum 3**:  
  - Generates all combinations of `k` numbers that sum to a target `n` from the range [1, 9], effectively using constraints to prune the solution space.