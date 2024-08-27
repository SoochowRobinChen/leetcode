class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        def backtrack(k, i, j):
            if k == len(word):
                return True
            
            if i < 0 or j < 0 or i >= row or j >= col or word[k] != board[i][j]:
                return False
            
            temp = board[i][j]
            # mark it as '#'
            board[i][j] = '#'

            found = backtrack(k + 1, i + 1, j) or backtrack(k + 1, i - 1, j) or backtrack(k + 1, i, j + 1) or backtrack(k + 1, i, j - 1)

            board[i][j] = temp

            return found
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if backtrack(0, i, j):
                        return True
        return False 
