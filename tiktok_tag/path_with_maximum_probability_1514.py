class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]
        prob = [0.0] * n
        prob[start_node] = 1.0

        # build graph
        for i, (s, e) in enumerate(edges):
            w = succProb[i]
            adj[s].append((e, w))
            adj[e].append((s, w))

        max_heap = [(-1.0, start_node)]

        """
        这一题用prob 数组，来确保不走回头路，
        因为probability肯定是小于1的
        肯定会越乘越小
        """
        while max_heap:
            cost, curr_node = heappop(max_heap)
            if curr_node == end_node:
                return -cost
            
            for nei, ncost in adj[curr_node]:
                ccost = -cost * ncost
                if ccost > prob[nei]:
                    prob[nei] = ccost
                    heappush(max_heap, (-ccost, nei))

        return 0.0