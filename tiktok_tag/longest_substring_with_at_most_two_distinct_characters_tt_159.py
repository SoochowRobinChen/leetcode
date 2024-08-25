class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Sliding window 的变种，只不过是设置了一个参数diff_count 为 2
        """
        window = defaultdict(int)
        left, right = 0, 0
        res = 0
        diff_count = 0

        while right < len(s):
            char = s[right]
            window[char] += 1
            right += 1

            if window[char] == 1:
                diff_count += 1

            while left < right and diff_count > 2:
                curr = s[left]
                window[curr] -= 1
                if window[curr] == 0:
                    diff_count -= 1
                left += 1
            
            res = max(res, right - left)
        
        return res 