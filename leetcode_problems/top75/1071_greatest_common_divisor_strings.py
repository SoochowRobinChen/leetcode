class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # we first check str1 + str2 == str2 + str1
        if str1 + str2 != str2 + str1:
            return ""
        
        from math import gcd
        # find gcd of two 
        return str1[:gcd(len(str1), len(str2))]