class NumArray:

    def __init__(self, nums: List[int]):
        # tricky point: add a 0 before hand
        self.preSum = [0]

        for i in range(len(nums)):
            self.preSum.append(self.preSum[-1] + nums[i])
        

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)