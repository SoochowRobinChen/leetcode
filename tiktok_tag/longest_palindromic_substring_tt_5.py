class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1: right]
        
        res = ''

        for i in range(len(s)):
            res_odd = helper(i, i)
            res_even = helper(i, i + 1)

            if len(res) < len(res_odd): res = res_odd
            if len(res) < len(res_even): res = res_even

        return res 