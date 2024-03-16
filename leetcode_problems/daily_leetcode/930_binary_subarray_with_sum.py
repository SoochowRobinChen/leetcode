class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        use prefix sum, to solve this problem 
        """

        total_count = 0
        curr_sum = 0
        freq = defaultdict(int)

        for num in nums:
            curr_sum += num
            if curr_sum == goal:
                total_count += 1
            
            if curr_sum - goal in freq:
                total_count += freq[curr_sum - goal]
            
            freq[curr_sum] += 1
        
        return total_count
        