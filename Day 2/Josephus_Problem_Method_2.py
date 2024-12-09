"""
Module to solve the Josephus problem using an optimized recursive method.
This approach improves the time complexity to O(n).
"""

def find_the_winner(n, k):
    """
    Determines the winner of the Josephus problem using an optimized approach.

    Args:
        n (int): Total number of participants.
        k (int): Step count for elimination.

    Returns:
        int: The position of the winner.

    Time Complexity:
        - O(n): Each recursive call performs a simple arithmetic operation, 
                and the recursion occurs n times.

    Space Complexity:
        - O(n): For the recursion stack in the worst case.
    """
    def josephus(n):
        """
        Recursive function to solve the Josephus problem in O(n) time.

        Args:
            n (int): Number of participants remaining.

        Returns:
            int: The position of the last remaining participant (0-indexed).

        Time Complexity:
            - O(n): One recursive call per participant.
        
        Space Complexity:
            - O(n): For the recursion stack in the worst case.
        """
        # Base case: When there is only one participant left
        if n == 1:
            return 0  # The 0-indexed position of the winner

        # Recursive case: Calculate the winner's position
        return (josephus(n - 1) + k) % n

    # Return the 1-indexed winner's position
    return josephus(n) + 1


if __name__ == "__main__":
    # Test the function with an example
    print(find_the_winner(4, 2))  # Output: 1
