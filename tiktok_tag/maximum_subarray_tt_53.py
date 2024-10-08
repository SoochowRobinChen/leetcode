class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        # init
        dp[0] = nums[0]

        for i in range(1, len(dp)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
    
    