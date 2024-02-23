class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)

        for index, num in enumerate(nums):
            rightSum -= num
            if leftSum == rightSum:
                return index
            # The reason why leftSum += num at this place 
            # since leftSum start from 0
            leftSum += num
        return -1