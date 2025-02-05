import heapq

def leastInterval(tasks, n):
    """
    Calculate the least number of intervals needed to schedule all tasks.

    Args:
        tasks (list): A list of task characters.
        n (int): The cooldown period between the same task.

    Returns:
        int: The least number of intervals needed to schedule all tasks.
    """
    if not tasks:
        return 0
    
    # Count the frequency of each task
    task_count = {}
    for task in tasks:
        task_count[task] = task_count.get(task, 0) + 1
    
    # Max-heap to store the frequency of tasks
    max_heap = [-count for count in task_count.values()]
    heapq.heapify(max_heap)

    time = 0
    while max_heap:
        temp = []
        for _ in range(n + 1):
            if max_heap:
                count = heapq.heappop(max_heap) + 1  # Decrease the count
                if count != 0:
                    temp.append(count)
            
        for item in temp:
            heapq.heappush(max_heap, item)

        time += n + 1 if max_heap else len(temp)

    return time
