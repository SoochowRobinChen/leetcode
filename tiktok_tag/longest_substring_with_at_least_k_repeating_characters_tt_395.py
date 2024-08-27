class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for i in range(1, len(set(s)) + 1):
            left, right = 0, 0
            times = [0] * 26
            diff_count, count = 0, 0

            while right < len(s):
                curr = ord(s[right]) - ord('a')
                times[curr] += 1
                if times[curr] == 1:
                    diff_count += 1
                if times[curr] == k:
                    count += 1
                right += 1

                while left < right and diff_count > i:
                    curr = ord(s[left]) - ord('a')
                    times[curr] -= 1
                    if times[curr] == 0:
                        diff_count -= 1
                    if times[curr] == k - 1:
                        count -= 1
                    left += 1
                
                if count == diff_count == i:
                    res = max(res, right - left)
        
        return res 
    