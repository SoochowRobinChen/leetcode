class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # dfs -> mark label 
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            """
            防止出现太多recursive, 应该用visited 数组标记
            """
            if board[i][j] == 'X' or visited[i][j]:
                return
            
            visited[i][j] = True

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(cols):
            dfs(0, i)
            dfs(rows - 1, i)
        
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        
        # mark not visited position to 'X'
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    board[i][j] = 'X'