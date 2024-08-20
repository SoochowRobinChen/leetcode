class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        m, res = 0, []
        for num in nums:
            m = max(num, m)
            res.append(m + num)
        
        # use python built-in function to accumulate the list
        return accumulate(res)