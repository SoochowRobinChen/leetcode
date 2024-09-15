class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            s, e = eq[0], eq[1]
            graph[s].append((e, values[i]))
            graph[e].append((s, 1.0 / values[i]))
        
        # use BFS
        def bfs(source, target):
            '这一点很妙，因为分子分母必须出现在graph中才会有答案'
            if source not in graph or target not in graph:
                return -1.0
            
            queue, visited = deque(), set()
            queue.append((source, 1.0))
            visited.add(source)

            while queue:
                curr, w = queue.popleft()
                if curr == target:
                    return w
                
                for nei, val in graph[curr]:
                    if nei not in visited:
                        queue.append((nei, val * w))
                        visited.add(nei)
            return -1.0
        
        return [bfs(q[0], q[1]) for q in queries]