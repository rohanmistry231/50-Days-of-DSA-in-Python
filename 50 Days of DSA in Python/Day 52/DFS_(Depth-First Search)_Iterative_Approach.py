def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")  # Visit the node (you can process it here)

            for neighbor in reversed(graph[node]):  # Reversed to maintain order of exploration
                if neighbor not in visited:
                    stack.append(neighbor)

# Example:
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}
dfs_iterative(graph, 0)  # Output: 0 2 1 4 3
