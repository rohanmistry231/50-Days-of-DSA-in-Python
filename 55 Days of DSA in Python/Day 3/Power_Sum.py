def power_sum(array, power=1):
    """
    Calculate the power sum of a nested list.

    The function recursively processes nested lists, summing elements
    at increasing power levels for each level of nesting.

    Parameters:
        array (list): A list of integers or nested lists.
        power (int, optional): The power level for the current recursion. Defaults to 1.

    Returns:
        int: The power sum of the input list.
    """
    # Initialize the running total to zero.
    total = 0

    # Iterate through each item in the input array.
    for item in array:
        # If the item is a list, recursively calculate its power sum.
        if isinstance(item, list):
            total += power_sum(item, power + 1)
        else:
            # Add the item's value directly to the total if it's not a list.
            total += item

    # Apply the power to the cumulative sum and return the result.
    return total ** power


if __name__ == "__main__":
    # Example usage
    nested_list = [1, [2, [3, 4]], 5]
    initial_power = 1
    print(f"The power sum of {nested_list} with initial power {initial_power} is: {power_sum(nested_list, initial_power)}")
