from typing import List

def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations of a list of numbers, including duplicates.

    Args:
        nums (List[int]): A list of integers that might contain duplicates.

    Returns:
        List[List[int]]: A list containing all unique permutations of the input list.

    Time Complexity:
        The time complexity is O(n * n!), where n is the length of the input list.
        - There are at most n! permutations.
        - However, duplicate elements reduce the number of unique permutations.
        - The function also uses a hash table for deduplication, which adds negligible overhead.
    """
    res = []  # List to store all unique permutations

    def permutations(index: int):
        """
        Recursive helper function to generate unique permutations.

        Args:
            index (int): Current index for permutation generation.
        """
        # Base case: if the current index is the last one, add the current permutation
        if index == len(nums) - 1:
            res.append(nums[:])  # Append a copy of nums to results
            return

        hash_set = {}  # Hash table to track duplicates in the current recursion
        for j in range(index, len(nums)):
            # Skip processing duplicate elements
            if nums[j] not in hash_set:
                hash_set[nums[j]] = True  # Mark the element as processed
                nums[index], nums[j] = nums[j], nums[index]  # Swap elements
                permutations(index + 1)  # Recurse for the next index
                nums[index], nums[j] = nums[j], nums[index]  # Backtrack (undo the swap)

    nums.sort()  # Sort the input to ensure duplicates are grouped
    permutations(0)  # Start the recursion from the first index
    return res

if __name__ == "__main__":
    # Example usage of the permute_unique function
    numbers = [1, 1, 2]
    unique_permutations = permute_unique(numbers)
    print("Unique permutations of", numbers, "are:")
    for perm in unique_permutations:
        print(perm)
