class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for pre in prerequisites:
            end, start = pre[0], pre[1]
            adj[start].append(end)
            indegree[end] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        node_visited = 0
        while q:
            curr = q.popleft()
            node_visited += 1
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return node_visited == numCourses