class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # to expand List
        """
        i % n 相当于扩展了整个环形数组
        """
        n = len(nums)
        stack = []
        res = [0] * n

        for i in range(2 * n - 1, -1, -1):
            while stack and nums[i % n] >= stack[-1]:
                stack.pop()
            res[i % n] = stack[-1] if stack else -1
            stack.append(nums[i % n])
        
        return res 