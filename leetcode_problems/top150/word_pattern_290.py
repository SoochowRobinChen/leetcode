class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, w_to_p = s.split(' '), {}

        if len(words) != len(pattern):
            return False
        
        """
        这一点很难想到
        """
        if len(set(pattern)) != len(set(words)): 
            return False
        
        for i in range(len(pattern)):
            if words[i] not in w_to_p:
                w_to_p[words[i]] = pattern[i]
            elif pattern[i] != w_to_p[words[i]]:
                return False

        return True 