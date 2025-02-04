from typing import List

def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations in `candidates` where the candidate numbers sum to `target`.
    Each number in `candidates` may only be used once in the combination.

    Args:
        candidates (List[int]): The list of candidate numbers.
        target (int): The target sum for the combinations.

    Returns:
        List[List[int]]: A list of unique combinations where the sum of numbers equals `target`.

    Time Complexity:
        O(2^n): In the worst case, we generate all subsets of the candidates list.

    Space Complexity:
        O(n): Space used for recursion stack and current combination.

    Example:
        Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
        Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    """
    # To store the resulting combinations
    result = []
    # Sort candidates to handle duplicates and enable early termination
    candidates.sort()

    def backtrack(index: int, current_sum: int, current_combination: List[int]) -> None:
        """
        Helper function to explore combinations using backtracking.

        Args:
            index (int): Current index in the candidates list.
            current_sum (int): The sum of the current combination.
            current_combination (List[int]): The current combination being built.
        """
        # If the current sum matches the target, add the combination to the result
        if current_sum == target:
            result.append(current_combination[:])  # Add a copy of the current combination
            return

        # If the current sum exceeds the target or we reach the end, terminate
        if current_sum > target or index >= len(candidates):
            return

        # Use a hash to track duplicates at the current level
        seen = {}
        for j in range(index, len(candidates)):
            # Skip duplicates at the same recursion level
            if candidates[j] in seen:
                continue

            # Mark the candidate as used in the current level
            seen[candidates[j]] = True

            # Include the candidate in the combination
            current_combination.append(candidates[j])
            # Recur with updated parameters: move to the next index and update the sum
            backtrack(j + 1, current_sum + candidates[j], current_combination)
            # Backtrack: remove the candidate from the combination
            current_combination.pop()

    # Start the backtracking process with an empty combination
    backtrack(0, 0, [])
    return result

if __name__ == "__main__":
    # Example usage
    input_candidates = [10, 1, 2, 7, 6, 1, 5]
    input_target = 8
    output = combination_sum_2(input_candidates, input_target)
    print(f"Unique combinations summing to {input_target}:")
    for combination in output:
        print(combination)
