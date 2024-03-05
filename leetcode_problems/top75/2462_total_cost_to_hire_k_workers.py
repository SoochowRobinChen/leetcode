class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pq1, pq2 = [], []
        left, right = 0, len(costs) - 1
        ans = 0

        while k > 0:
            while left < right and len(pq1) < candidates: 
                heapq.heappush(pq1, (costs[left], left))
                left += 1
            while left < right and len(pq2) < candidates: 
                heapq.heappush(pq2, (costs[right], right))
                right -= 1
            
            if not pq1:
                ans += heapq.heappop(pq2)[0]
            elif not pq2:
                ans += heapq.heappop(pq1)[0]
                # make sure that right side should <=
            elif pq1[0][0] <= pq2[0][0]:
                ans += heapq.heappop(pq1)[0]
            else:
                ans += heapq.heappop(pq2)[0]
            
            k -= 1
        
        return ans
