
def findMaxFish(grid):
    def dfs(x,y):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
            return 0
        
        fish = grid[x][y] 
        grid[x][y]  = 0 

        fish += dfs(x + 1, y)
        fish += dfs(x - 1, y)
        fish += dfs(x, y + 1)
        fish += dfs(x, y - 1)
        return fish
        
    m,n = len(grid), len(grid[0])
    max_fish = 0 

    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0:
                max_fish = max(max_fish, dfs(i, j))
    return max_fish

grid = [[0, 2, 1, 0], 
        [4, 0, 0, 3], 
        [1, 0, 0, 4], 
        [0, 3, 2, 0]]
print(findMaxFish(grid))