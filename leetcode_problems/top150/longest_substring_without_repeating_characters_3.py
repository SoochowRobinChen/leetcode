class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        left, right = 0, 0
        res = 0

        while right < len(s):
            curr = s[right]
            window[curr] += 1
            right += 1
            while window[curr] > 1:
                temp = s[left]
                window[temp] -= 1
                left += 1
            
            res = max(res, right - left)

        return res 