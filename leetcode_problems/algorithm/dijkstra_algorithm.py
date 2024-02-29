"""
Dijkstra algorithm is greedy Bread First Search(BFS) algorithm 
to find shortest path in a directed graph.
Make sure that the weight value should be larger than 0.
If weight value is smaller than 0, we need to use Bellman-Ford.

And Dijkstra's algorithm can be used to determine the shortest path
from one node in a graph to every node within the same graph data
structure, provided that nodes are reachable from starting point. 
"""
from collections import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        # construct adjency list
        for s, d, weight in edges:
            adj[s].append([d, weight])
        
        shortest = {} # Map vertext -> dist of shortest path
        minHeap = [[0, src]] # init a starting point with weight

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])

        # how to handle some unvisited nodes:
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest