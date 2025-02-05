from typing import List

def non_overlapping_intervals(intervals: List[List[int]]) -> int:
    """
    Finds the minimum number of intervals to remove to eliminate overlaps.
    
    Args:
        intervals (list): List of intervals [start, end].
    
    Returns:
        int: Minimum number of intervals to remove.
    """
    if not intervals:
        return 0
    
    # Sort by ending times
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    prev_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            # Overlapping interval, remove it
            count += 1
        else:
            # Update previous end time
            prev_end = intervals[i][1]
    
    return count
