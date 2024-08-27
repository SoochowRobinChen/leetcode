class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time complexity is M * N 
        # Space complexity is M * N 
        rows, cols = len(grid), len(grid[0])

        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count 