from typing import List

def two_city_scheduling(costs: List[List[int]]) -> int:
    """
    Minimizes the cost of sending people to two cities.
    
    Args:
        costs (list): List of [costA, costB] for each person.
    
    Returns:
        int: Minimum total cost.
    """
    # Sort by cost difference between City A and City B
    costs.sort(key=lambda x: x[0] - x[1])
    
    total_cost = 0
    n = len(costs) // 2
    
    # First n people go to City A, rest to City B
    for i in range(n):
        total_cost += costs[i][0]  # City A
    for i in range(n, 2 * n):
        total_cost += costs[i][1]  # City B
    
    return total_cost
