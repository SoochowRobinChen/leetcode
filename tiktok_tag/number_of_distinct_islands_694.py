class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
        忘记加visited set，导致重复计算
        """
        diff_set = set()
        seen = set()
        row, col = len(grid), len(grid[0])

        def dfs(i, j, label):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return
            
            if (i, j) in seen:
                return

            path.append(label)
            seen.add((i, j))
            dfs(i + 1, j, 'R')
            dfs(i - 1, j, 'L')
            dfs(i, j + 1, 'D')
            dfs(i, j - 1, 'U')
            # mark end 
            path.append('E')


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in seen:
                    path = []
                    dfs(i, j, 'S')
                    diff_set.add(tuple(path))


        return len(diff_set)