from typing import List

def min_arrows_to_burst_balloons(points: List[List[int]]) -> int:
    """
    Finds the minimum number of arrows required to burst all balloons.
    
    Args:
        points (list): List of balloon intervals [x_start, x_end].
    
    Returns:
        int: Minimum number of arrows needed.
    """
    if not points:
        return 0
    
    # Sort balloons by end position
    points.sort(key=lambda x: x[1])
    
    arrows = 1
    last_arrow_pos = points[0][1]
    
    for start, end in points[1:]:
        if start > last_arrow_pos:
            arrows += 1
            last_arrow_pos = end
    
    return arrows
