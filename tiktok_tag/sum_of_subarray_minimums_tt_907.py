class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        与2104题目很像，利用单调栈来处理
        """
        stack = []
        res = 0
        
        for right in range(len(arr) + 1):

            while stack and (right == len(arr) or arr[right] <= arr[stack[-1]]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                res += arr[mid] * (mid - left) * (right - mid)
            
            stack.append(right)
        
        return res % (10 ** 9 + 7)