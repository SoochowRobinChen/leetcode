class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(nums, path):
            if not nums:
                permutations.append(list(path))
                return
            
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(nums[:i] + nums[i + 1:], path)
                path.pop()
        
        backtrack(nums, [])

        return permutations