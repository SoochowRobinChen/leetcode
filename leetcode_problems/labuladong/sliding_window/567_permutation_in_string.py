class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = Counter(s1), defaultdict(int)
        require, valid = len(need), 0
        left, right = 0, 0

        while right < len(s2):
            temp = s2[right]
            window[temp] += 1
            right += 1

            if temp in need and window[temp] == need[temp]:
                valid += 1
            
            while right - left >= len(s1):
                if valid == require:
                    return True
                temp = s2[left]
                if temp in need and window[temp] == need[temp]:
                    valid -= 1
                window[temp] -= 1
                left += 1
        
        return False