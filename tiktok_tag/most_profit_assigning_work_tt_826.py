class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        res, best = 0, 0

        diff_profit_pairs = [(diff, pro) for diff, pro in zip(difficulty, profit)]

        # sort
        diff_profit_pairs.sort()
        worker.sort()

        j = 0

        for w in worker:
            while j < len(diff_profit_pairs) and w >= diff_profit_pairs[j][0]:
                best = max(best, diff_profit_pairs[j][1])
                j += 1
            
            res += best
        
        return res 