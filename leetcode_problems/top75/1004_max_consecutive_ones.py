class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # use sliding window to solve this problem
        left, right = 0, 0
        windowOnes = 0
        res = 0

        while right < len(nums):
            if nums[right] == 1:
                windowOnes += 1
            right += 1

            while right - left - windowOnes > k:
                if nums[left] == 1:
                    windowOnes -= 1
                left += 1
            
            res = max(res, right - left)
        
        return res
    