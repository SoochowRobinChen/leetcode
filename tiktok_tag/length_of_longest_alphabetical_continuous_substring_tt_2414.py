class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        count = 1
        res = 1

        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                count += 1
                res = max(res, count)
            else:
                count = 1
        
        return res 