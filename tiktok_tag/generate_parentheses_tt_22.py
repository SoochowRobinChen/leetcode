class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        choice = ['(', ')']

        def backtrack(left, right, curr):
            if left > right:
                return 

            if left < 0 or right < 0:
                return 
            
            if left == 0 and right == 0:
                res.append(''.join(curr))
                return

            for c in choice:
                curr.append(c)
                if c == '(':
                    backtrack(left - 1, right, curr)
                else:
                    backtrack(left, right - 1, curr)
                curr.pop()
        
        backtrack(n, n, [])

        return res 