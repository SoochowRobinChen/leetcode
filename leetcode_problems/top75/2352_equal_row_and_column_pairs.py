class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = {}
        res = 0

        for row in grid:
            count[tuple(row)] = count.get(tuple(row), 0) + 1
        
        for i in range(len(grid)):
            col = [r[i] for r in grid]
            if col in grid:
                res += count[tuple(col)]
        
        return res