class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1.build graph
        adj = [[] for i in range(n)]
        for u, v, w in times:
            adj[u-1].append((v-1, w))
        
        # 2. initialize distance array and starting point
        dis = [float('inf')] * n
        dis[k-1] = 0

        # 3. use a min heap to process the shortest travel times first
        heap = [(0, k -1)]

        while heap:
            time, node = heappop(heap)

            for nei, travel_time in adj[node]:
                new_time = time + travel_time 
                if new_time < dis[nei]:
                    dis[nei] = new_time
                    heappush(heap, (new_time, nei))
        
        # check if all nodes are reachable
        max_time = max(dis)
        return max_time if max_time != float('inf') else -1