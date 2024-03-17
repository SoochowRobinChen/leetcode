class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # count, 0: -1, 1: 1, if count = 0 means are equal
        memo = defaultdict(int)
        memo[0] = -1
        count = 0
        max_length = 0

        for i in range(len(nums)):
            count += nums[i] if nums[i] == 1 else -1
            if count in memo:
                max_length = max(max_length, i - memo[count])
            else:
                memo[count] = i
        
        return max_length