from typing import List

def subsets_with_duplicates(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets (the power set) of a given list with handling for duplicates using backtracking.

    Args:
        nums (List[int]): A list of integers, which may include duplicates.

    Returns:
        List[List[int]]: A list containing all unique subsets of the input list.

    Time Complexity:
        O(2^n): Each element can either be included or excluded, resulting in 2^n subsets.
        Sorting the input adds an additional O(n log n) complexity.

    Space Complexity:
        O(n): The recursion stack can go as deep as the number of elements in the list.
    """
    # List to store all unique subsets
    result = []

    # Sort the input list to handle duplicates
    nums.sort()

    def backtrack(index: int, current_subset: List[int]):
        """
        Backtracking helper function to generate subsets.

        Args:
            index (int): The current index in the list being processed.
            current_subset (List[int]): The current subset being constructed.

        Time Complexity:
            O(2^n): Each recursive call represents either including or excluding an element.

        Space Complexity:
            O(n): Due to the recursion stack and the subset list.
        """
        # Base Case: If all elements have been considered
        if index == len(nums):
            result.append(current_subset[:])  # Append a copy of the current subset
            return

        # Include the current element
        current_subset.append(nums[index])
        backtrack(index + 1, current_subset)
        current_subset.pop()  # Backtrack to exclude the last element

        # Exclude the current element and skip duplicates
        while index < len(nums) - 1 and nums[index] == nums[index + 1]:
            index += 1
        backtrack(index + 1, current_subset)

    # Initialize the recursion with an empty subset
    backtrack(0, [])
    return result

if __name__ == "__main__":
    # Example usage of the subsets_with_duplicates function
    numbers = [1, 2, 2]
    unique_subsets = subsets_with_duplicates(numbers)
    print("Unique subsets of", numbers, "are:")
    for subset in unique_subsets:
        print(subset)
