class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        max_sum = window

        for i in range(len(nums) - k):
            window = window - nums[i] + nums[i + k]
            max_sum = max(max_sum, window)
        
        return max_sum / k