def num_islands(grid):
    if not grid:
        return 0

    def dfs(i, j):
        # Check boundaries and water
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        # Mark the land as visited
        grid[i][j] = '0'
        # Explore all 4 directions (up, down, left, right)
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':  # Found an unvisited land cell
                dfs(i, j)  # Perform DFS to mark all connected land cells
                count += 1  # Increment the island count

    return count

# Example:
grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
print(num_islands(grid))  # Output: 1
