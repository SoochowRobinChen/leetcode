class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                length = i - left - 1
                res = max(res, heights[mid] * length)
            stack.append(i)

        """
        要考虑到可能栈里还有元素
        """

        while stack:
            mid = stack.pop()
            left = -1 if not stack else stack[-1]
            length = len(heights) - left - 1
            res = max(res, heights[mid] * length)
        
        return res 