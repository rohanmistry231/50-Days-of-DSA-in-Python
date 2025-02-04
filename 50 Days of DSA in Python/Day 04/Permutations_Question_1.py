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
