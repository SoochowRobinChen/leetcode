class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # stack in an increasing 
        stack = []
        res = 0

        for right in range(len(arr) + 1):
            while stack and (right == len(arr) or arr[right] <= arr[stack[-1]]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                res += (mid - left) * (right - mid) * arr[mid]
            
            stack.append(right)
        
        return res % (10 ** 9 + 7)