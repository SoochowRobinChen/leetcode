class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """
        这一题的思路就是首先先建图，
        然后对每个点都做一次dijkstra算法，找出这个点到其他点的最短距离
        然后根据这个最短距离来判断
        """
        # create graph
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # dijkstra
        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0
            pq = [(0, start)]

            while pq:
                curr_dis, u = heapq.heappop(pq)

                if curr_dis > dist[u]:
                    continue
                
                for v, w in graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
            
            return dist
        
        min_reachable_cities = float('inf')
        city = -1

        # from small to large
        for i in range(n):
            dist = dijkstra(i)
            reachable_cities = sum(d <= distanceThreshold for d in dist)

            if reachable_cities <= min_reachable_cities:
                min_reachable_cities = reachable_cities
                city = i
        
        return city 