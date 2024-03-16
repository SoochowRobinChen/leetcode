class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])

        self.preSum = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        # iterate and calculate presum
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                self.preSum[i][j] = matrix[i - 1][j - 1] + self.preSum[i-1][j] + self.preSum[i][j-1] - self.preSum[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2 + 1][col2 + 1] - self.preSum[row1][col2 + 1] - self.preSum[row2 + 1][col1] + self.preSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)