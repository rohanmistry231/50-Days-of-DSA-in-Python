from typing import List

def num_rescue_boats(people: List[int], limit: int) -> int:
    """
    Finds the minimum number of boats needed to save people.
    
    Args:
        people (list): List of people's weights.
        limit (int): Maximum weight a boat can carry.
    
    Returns:
        int: Minimum number of boats required.
    """
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # Take the lighter person as well
        right -= 1  # Always take the heavier person
        boats += 1
    
    return boats
