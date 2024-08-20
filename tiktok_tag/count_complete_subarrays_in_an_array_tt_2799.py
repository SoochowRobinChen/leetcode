class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        freq = defaultdict(int)

        res = 0
        # slding window to solve this problem 
        left, right = 0, 0

        while right < len(nums):
            freq[nums[right]] += 1

            while len(freq) == distinct:
                res += len(nums) - right

                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                
                left += 1
            
            right += 1
        
        return res 