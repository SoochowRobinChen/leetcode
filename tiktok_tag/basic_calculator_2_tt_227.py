class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = '+'
        operators = {'+', '-', '*', '/'}
        curr_num = 0

        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            # this line need to remember 
            if char in operators or i == len(s) - 1:
                if op == '+':
                    stack.append(curr_num)
                elif op == '-':
                    stack.append(-curr_num)
                elif op == '*':
                    value = stack.pop() * curr_num
                    stack.append(value)
                elif op == '/':
                    value = int(stack.pop() / curr_num)
                    stack.append(value)
                
                curr_num = 0
                op = char
        
        return sum(stack)