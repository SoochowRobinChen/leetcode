class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, window = Counter(p), defaultdict(int)
        require, valid = len(need), 0
        left, right = 0, 0
        res = []

        while right < len(s):
            temp = s[right]
            window[temp] += 1
            right += 1
            if temp in need and window[temp] == need[temp]:
                valid += 1

            while right - left >= len(p):
                if valid == require:
                    res.append(left)
                
                temp = s[left]
                if temp in need and window[temp] == need[temp]:
                    valid -= 1
                
                window[temp] -= 1
                left += 1
        
        return res