class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        curr_sum = 0
        count = 0
        # init
        # Do not forget to add initial value
        # to the prefix map
        prefix_map[0] = 1

        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_map:
                count += prefix_map[curr_sum - k]
        

            prefix_map[curr_sum] += 1
        
        return count 