"""
Module to solve the Josephus problem.
The problem is to find the winner in a circular game where every k-th person is eliminated.
"""

def find_the_winner(n, k):
    """
    Determines the winner of the Josephus problem.

    Args:
        n (int): Total number of participants.
        k (int): Step count for elimination.

    Returns:
        int: The position of the winner.

    Time Complexity:
        - O(n^2) in the worst case, due to repeated list modifications during recursion.
          Each `del` operation in a list takes O(n) time, and it is called recursively n times.

    Space Complexity:
        - O(n) for storing the participants list.
        - O(n) for the recursion stack in the worst case.

        Overall space complexity: O(n).
    """
    # Create a list of participants numbered from 1 to n
    participants = [i + 1 for i in range(n)]

    def helper(participants_list, start_index):
        """
        Recursive helper function to eliminate participants.

        Args:
            participants_list (list): Current list of participants.
            start_index (int): Index to start the elimination.

        Returns:
            int: The position of the last remaining participant.

        Time Complexity:
            - Each call removes one participant, taking O(n) for deletion.
              Recursion occurs n times, making the total O(n^2).

        Space Complexity:
            - O(n) for the recursion stack and participant list in memory.
        """
        # Base case: When only one participant remains
        if len(participants_list) == 1:
            return participants_list[0]

        # Calculate the index of the participant to remove
        index_to_remove = (start_index + k - 1) % len(participants_list)

        # Remove the participant from the list
        del participants_list[index_to_remove]

        # Recursively call the helper with the updated list and start index
        return helper(participants_list, index_to_remove)

    # Start the recursive elimination process
    return helper(participants, 0)


if __name__ == "__main__":
    # Test the function with an example
    print(find_the_winner(4, 2))  # Output: 1
