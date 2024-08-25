class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n, stack = len(nums), []
        ans = 0

        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                ans -= (right - mid) * (mid - left) * nums[mid]
            stack.append(right)
        
        stack.clear()

        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                ans += (right - mid) * (mid - left) * nums[mid]
            stack.append(right)

        return ans 
