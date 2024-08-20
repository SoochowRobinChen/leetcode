class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        self.res = float('inf')

        def dfs(cur, moves):
            if moves > self.res:
                return
            
            if cur == 9:
                self.res = min(self.res, moves)
                return
            
            i, j = cur // 3, cur % 3
            if grid[i][j] != 0:
                dfs(cur + 1, moves)
                return
            
            for x in range(3):
                for y in range(3):
                    if grid[x][y] <= 1:
                        continue
                    grid[x][y] -= 1
                    grid[i][j] += 1

                    dfs(cur + 1, moves + abs(x - i) + abs(y - j))

                    grid[x][y] += 1
                    grid[i][j] -= 1
        
        dfs(0, 0)

        return self.res 