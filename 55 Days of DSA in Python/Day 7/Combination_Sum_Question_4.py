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
    # To store the resulting combinations
    result = []

    def backtrack(start: int, current_combination: List[int], current_sum: int) -> None:
        """
        Helper function to explore combinations using backtracking.

        Args:
            start (int): The starting number for the current recursion.
            current_combination (List[int]): The current combination being built.
            current_sum (int): The sum of the current combination.
        """
        # If the current combination meets the conditions, add it to the result
        if current_sum == n and len(current_combination) == k:
            result.append(current_combination[:])  # Add a copy of the current combination
            return

        # If the sum exceeds n or the combination size exceeds k, terminate
        if current_sum > n or len(current_combination) == k:
            return

        # Iterate through the possible numbers, ensuring no repeats
        for number in range(start, 10):
            # Include the current number in the combination
            current_combination.append(number)
            # Recur with updated parameters
            backtrack(number + 1, current_combination, current_sum + number)
            # Backtrack: remove the number from the combination
            current_combination.pop()

    # Start the backtracking process with an empty combination
    backtrack(1, [], 0)
    return result

if __name__ == "__main__":
    # Example usage
    k_value = 3
    target_sum = 7
    output = combination_sum_3(k_value, target_sum)
    print(f"Combinations of {k_value} numbers summing to {target_sum}:")
    for combination in output:
        print(combination)
