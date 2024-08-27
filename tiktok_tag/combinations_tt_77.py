class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            if len(path) == k:
                res.append(list(path))
                return
            
            for i in range(index, n + 1):

                path.append(i)

                backtrack(i + 1, path)

                path.pop()
        
        backtrack(1, [])

        return res 