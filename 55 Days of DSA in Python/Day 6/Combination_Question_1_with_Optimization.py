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

if __name__ == "__main__":
    n_value = 4
    k_value = 2
    result = find_combinations_optimized(n_value, k_value)
    print(f"All {k_value}-combinations of numbers from 1 to {n_value} are:")
    for combination in result:
        print(combination)
