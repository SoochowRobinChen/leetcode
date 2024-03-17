class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def count(left, right):
            if left > right:
                return 1
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            res = 0
            for i in range(left, right + 1):
                left_num = count(left, i - 1)
                right_num = count(i + 1, right)

                res += left_num * right_num
            
            memo[(left, right)] = res

            return res
        
        return count(1, n)