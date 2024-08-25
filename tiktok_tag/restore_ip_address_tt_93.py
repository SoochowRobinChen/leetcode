class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # corner case
        if len(s) > 12: return []
        res = []

        def backtrack(index, dots, curr_ip):
            if index == len(s) and dots == 4:
                # remove last dots
                res.append(curr_ip[:-1])
                return 
            
            if dots > 4:
                return

            
            for j in range(index, min(index + 3, len(s))):
                if int(s[index:j+1]) < 256 and (j == index or s[index] != '0'):
                    backtrack(j + 1, dots + 1, curr_ip + s[index:j+1] + '.')
            
        
        backtrack(0, 0, '')

        return res 