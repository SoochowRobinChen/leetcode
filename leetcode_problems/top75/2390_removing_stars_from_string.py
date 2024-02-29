class Solution:
    def removeStars(self, s: str) -> str:
        # use stack 
        stack = []
        position = 0
        while position < len(s):
            if s[position] != '*':
                stack.append(s[position])
            else:
                stack.pop()
        
            position += 1
        
        return "".join(stack)
    