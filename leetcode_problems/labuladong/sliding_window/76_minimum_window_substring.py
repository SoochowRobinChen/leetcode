class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, require = Counter(t), 0
        valid = len(need)
        window = defaultdict(int)
        left, right = 0, 0
        ans = (float('inf'), 0, 0)

        while right < len(s):
            curr_str = s[right]
            window[curr_str] += 1
            right += 1

            if curr_str in need and window[curr_str] == need[curr_str]:
                require += 1
            
            while valid == require and left < right:
                # shrink 
                temp = s[left]

                if right - left < ans[0]:
                    ans = (right - left, left, right)

                if temp in need and window[temp] == need[temp]:
                    require -= 1
                
                window[temp] -= 1
                left += 1
        
        return '' if ans[0] == float('inf') else s[ans[1]: ans[2]]