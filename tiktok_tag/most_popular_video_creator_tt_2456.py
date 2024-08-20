class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        total = defaultdict(int)
        best = {}

        for creator, i, view in zip(creators, ids, views):
            total[creator] += view

            if creator not in best:
                best[creator] = (i, view)
            elif view > best[creator][1]:
                best[creator] = (i, view)
            elif view == best[creator][1] and i < best[creator][0]:
                best[creator] = (i, view)

        
        # find max value
        highest = max(total.values())
        res = []

        for c in total.keys():
            if total[c] == highest:
                res.append((c, best[c][0]))
        
        return res 