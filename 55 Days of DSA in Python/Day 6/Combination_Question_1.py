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

if __name__ == "__main__":
    n, k = 4, 2
    result = generate_combinations(n, k)
    print(f"Combinations of {k} numbers from 1 to {n} are:")
    for combination in result:
        print(combination)
