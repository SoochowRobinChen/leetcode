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
                left_count = count(left, i - 1)
                right_count = count(i + 1, right)

                res += left_count * right_count
            
            memo[(left, right)] = res

            return res
        
        return count(1, n)

