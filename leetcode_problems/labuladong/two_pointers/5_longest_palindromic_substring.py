class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1: right]
        
        res = ''

        for i in range(len(s)):
            s_odd = helper(i, i)
            s_even = helper(i, i + 1)

            if len(s_odd) > len(res): res = s_odd
            if len(s_even) > len(res): res = s_even
        
        return res
