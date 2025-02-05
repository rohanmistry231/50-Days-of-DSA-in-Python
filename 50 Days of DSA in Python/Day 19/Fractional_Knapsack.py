from typing import List, Tuple

def fractional_knapsack(items: List[Tuple[int, int]], capacity: int) -> float:
    """
    Solves the Fractional Knapsack problem using a greedy approach.
    
    Args:
        items (list): List of tuples where each tuple (value, weight).
        capacity (int): Maximum weight the knapsack can hold.
    
    Returns:
        float: Maximum total value possible.
    """
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item[0] / item[1], reverse=True)
    
    total_value = 0.0
    
    for value, weight in items:
        if capacity >= weight:
            # Take the full item
            capacity -= weight
            total_value += value
        else:
            # Take the fraction of the item
            total_value += (value / weight) * capacity
            break
    
    return total_value
