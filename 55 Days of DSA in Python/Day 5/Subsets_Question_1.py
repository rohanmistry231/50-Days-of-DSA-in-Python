from typing import List

def power_set(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets (the power set) of a given list using backtracking.

    Args:
        nums (List[int]): A list of integers for which to generate subsets.

    Returns:
        List[List[int]]: A list containing all subsets of the input list.

    Time Complexity:
        O(2^n): Each element in the list can either be included or excluded, 
        resulting in 2^n subsets for a list of size n.

    Space Complexity:
        O(n): The recursion stack can go as deep as the number of elements in the list.
    """
    # List to store all subsets
    output = []

    def helper(nums: List[int], i: int, subset: List[int]):
        """
        Helper function to recursively generate subsets.

        Args:
            nums (List[int]): The input list of integers.
            i (int): The current index in the list being processed.
            subset (List[int]): The current subset being constructed.

        Time Complexity:
            Each recursive call either includes or excludes an element, 
            resulting in a total of O(2^n) calls.

        Space Complexity:
            O(n): Due to the recursion stack and the subset list.
        """
        # Base Case: If we have processed all elements
        if i == len(nums):
            output.append(subset.copy())  # Append a copy of the current subset
            return

        # Recursive Case 1: Exclude the current element
        helper(nums, i + 1, subset)

        # Recursive Case 2: Include the current element
        subset.append(nums[i])
        helper(nums, i + 1, subset)

        # Backtrack to remove the element added in this recursion
        subset.pop()

    # Initialize the recursion with an empty subset
    helper(nums, 0, [])
    return output

if __name__ == "__main__":
    # Example usage of the power_set function
    numbers = [1, 2, 3]
    subsets = power_set(numbers)
    print("Power set of", numbers, "is:")
    for subset in subsets:
        print(subset)
