def canCompleteCircuit(gas, cost):
    """
    Determine if a trip around the circuit is possible starting from a gas station.

    Args:
        gas (list): A list of gas available at each station.
        cost (list): A list of gas required to reach the next station.

    Returns:
        int: The index of the starting station, or -1 if not possible.
    """
    total_gas = 0
    current_gas = 0
    start_index = 0

    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]

        # If the current gas is negative, reset the start index
        if current_gas < 0:
            start_index = i + 1
            current_gas = 0

    return start_index if total_gas >= 0 else -1
