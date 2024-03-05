class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for num in nums:
            temp = max(prev + num, curr)
            prev = curr
            curr = temp
        return curr