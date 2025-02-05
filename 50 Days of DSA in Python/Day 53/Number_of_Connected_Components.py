def count_connected_components(graph):
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    count = 0
    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1

    return count

# Example:
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3],
    5: []
}
print(count_connected_components(graph))  # Output: 3
