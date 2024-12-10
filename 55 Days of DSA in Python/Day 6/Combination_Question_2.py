from typing import List

def find_combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations of candidates where the candidate numbers sum to the target.

    Each number in candidates may be used an unlimited number of times in a combination.

    Args:
        candidates (List[int]): The list of candidate numbers.
        target (int): The target sum.

    Returns:
        List[List[int]]: A list of all unique combinations where the sum equals the target.

    Time Complexity:
        O(2^n): Each candidate can be included or excluded, leading to exponential growth.

    Space Complexity:
        O(target / min(candidates)): The recursion stack depth depends on the smallest candidate.

    Example:
        Input: candidates = [2, 3, 6, 7], target = 7
        Output: [[2, 2, 3], [7]]
    """
    combinations = []

    def backtrack(start: int, current_combination: List[int], current_sum: int) -> None:
        """
        Helper function to generate combinations using backtracking.

        Args:
            start (int): The starting index for the current recursion.
            current_combination (List[int]): The current combination being built.
            current_sum (int): The current sum of the numbers in the combination.
        """
        # If the current sum exceeds the target, backtrack
        if current_sum > target:
            return

        # If the current sum equals the target, save the combination
        if current_sum == target:
            combinations.append(current_combination[:])  # Add a copy of the current combination
            return

        # Explore further by adding numbers to the combination
        for i in range(start, len(candidates)):
            # Include the current candidate
            current_combination.append(candidates[i])
            backtrack(i, current_combination, current_sum + candidates[i])

            # Exclude the current candidate (backtrack)
            current_combination.pop()

    # Start backtracking with an empty combination
    backtrack(0, [], 0)
    return combinations

if __name__ == "__main__":
    candidates_list = [2, 3, 6, 7]
    target_value = 7
    result = find_combination_sum(candidates_list, target_value)
    print(f"Combinations that sum to {target_value} are:")
    for combination in result:
        print(combination)
