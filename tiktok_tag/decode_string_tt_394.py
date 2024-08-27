class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            char = s[i]
            if char != ']':
                stack.append(char)
            else:
                temp_num, temp_s = '', ''
                while stack and stack[-1] != '[':
                    temp_s = stack.pop() + temp_s
                
                # pop [
                stack.pop()
                while stack and stack[-1].isdigit():
                    temp_num = stack.pop() + temp_num
                
                stack.append(int(temp_num) * temp_s)
        
        return ''.join(stack)