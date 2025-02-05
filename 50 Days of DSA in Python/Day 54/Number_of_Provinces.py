def find_provinces(graph):
    visited = set()

    def dfs(city):
        visited.add(city)
        for neighbor in graph[city]:
            if neighbor not in visited:
                dfs(neighbor)

    count = 0
    for city in range(len(graph)):
        if city not in visited:
            dfs(city)
            count += 1

    return count

# Example:
graph = [
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 1, 1]
]
print(find_provinces(graph))  # Output: 2
