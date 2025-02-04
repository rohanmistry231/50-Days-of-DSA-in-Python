def find_the_winner(n, k):
    """
    Finds the winner of the Josephus problem using an iterative approach.

    The problem is solved by simulating the elimination process iteratively,
    ensuring (O(1)) space complexity.

    Args:
        n (int): The total number of people in the circle.
        k (int): The step count for elimination.

    Returns:
        int: The position of the survivor (1-indexed).

    Time Complexity:
        O(n): The loop iterates (n - 1) times.
    Space Complexity:
        O(1): No additional space is used beyond variables.
    """
    # Initialize the survivor's position (0-indexed).
    survivor = 0

    # Iteratively calculate the survivor's position.
    for i in range(2, n + 1):
        survivor = (survivor + k) % i

    # Convert the survivor's position to 1-indexed.
    return survivor + 1


if __name__ == "__main__":
    # Example usage
    total_people = 5
    step_count = 3
    print(f"The winner is at position: {find_the_winner(total_people, step_count)}")
