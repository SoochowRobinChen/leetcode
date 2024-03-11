class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(index, path, target):
            if target == 0:
                res.append(list(path))
                return
            elif target < 0:
                return
            else:
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i-1]:
                        continue
                    
                    path.append(candidates[i])
                    target -= candidates[i]

                    backtrack(i + 1, path, target)

                    path.pop()
                    target += candidates[i]
        
        backtrack(0, [], target)
        
        return res
