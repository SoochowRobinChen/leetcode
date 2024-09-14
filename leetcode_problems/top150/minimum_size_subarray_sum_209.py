class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = 0 # calculate sum
        left, right = 0, 0
        res = float('inf')

        while right < len(nums):
            window += nums[right]
            right += 1
            while window >= target:
                res = min(res, right - left)

                window -= nums[left]
                left += 1
                
        return 0 if res == float('inf') else res