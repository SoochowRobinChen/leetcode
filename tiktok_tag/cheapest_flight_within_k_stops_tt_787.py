class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edge = defaultdict(list)
        for u, v, w in flights:
            edge[u].append((v, w))
        
        dist = dict()

        q = [(0, src, 0)] # cost, curr, stop

        while q:
            cost, curr, stop = heapq.heappop(q)
            if stop > k + 1 or cost > dist.get((curr, stop), float('inf')):
                continue
            if curr == dst:
                return cost
            
            for nxt, w in edge[curr]:
                tmp = cost + w
                if tmp < dist.get((nxt, stop + 1), float('inf')):
                    heapq.heappush(q, (tmp, nxt, stop + 1))
                    dist[(nxt, stop + 1)] = tmp
        
        return -1