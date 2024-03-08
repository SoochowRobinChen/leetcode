class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(num, stack, target):
            if len(stack) == k and target == 0:
                res.append(stack)
                return
            
            for x in range(num + 1, 10):
                if x <= target:
                    # stack + [x] will create a new copy of list
                    backtrack(x, stack + [x], target - x)
                else:
                    return
        
        backtrack(0, [], n)

        return res