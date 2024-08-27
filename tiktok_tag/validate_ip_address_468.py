class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # Time O(N) 
        # Space O(N)

        def is_ip_v4(s):   
            address = s.split(".")
            if len(address) != 4: return False 
            for item in address: 
                "非常有意思的点是 怎么怎么判断一个字符串是不是有leading zero"
                if not item.isdigit() or str(int(item)) != item or int(item) > 255:
                    return False 
            return True 

        def is_ip_v6(s): 
            address = s.split(":")
            if len(address) != 8: return False 
            for item in address: 
                if len(item) < 1 or len(item) > 4: return False 
                for ch in item.lower(): 
                    if 'a' <= ch <= 'f' or '0' <= ch <= '9': 
                        continue 
                    else: 
                        return False
            return True 

        if is_ip_v4(queryIP): return "IPv4" 
        return "IPv6" if is_ip_v6(queryIP) else "Neither"