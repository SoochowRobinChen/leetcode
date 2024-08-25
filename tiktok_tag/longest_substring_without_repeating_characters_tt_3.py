class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        left, right = 0, 0
        res = 0

        while right < len(s):
            temp = s[right]
            window[temp] += 1
            right += 1

            while window[temp] > 1:
                curr = s[left]
                window[curr] -= 1
                left += 1
            
            res = max(res, right - left)
        
        return res 