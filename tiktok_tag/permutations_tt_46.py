class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        use used[] to record whether the number is used or not
        """
        res = []
        used = [False] * len(nums)

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path, used)

                used[i] = False
                path.pop()
        
        backtrack([], used)

        return res 