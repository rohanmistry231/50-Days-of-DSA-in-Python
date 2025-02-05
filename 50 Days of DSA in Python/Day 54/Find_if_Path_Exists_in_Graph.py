def path_exists(graph, start, target):
    visited = set()

    def dfs(node):
        if node == target:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    return dfs(start)

# Example:
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: []
}
print(path_exists(graph, 0, 3))  # Output: True
print(path_exists(graph, 1, 3))  # Output: True
print(path_exists(graph, 0, 4))  # Output: False
