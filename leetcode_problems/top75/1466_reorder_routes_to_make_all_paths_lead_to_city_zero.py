class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # build adjencency list
        edge = defaultdict(list)
        for x, y in connections:
            edge[x].append((y, 1))
            edge[y].append((x, 0))
        
        res = 0
        stack = [(0, -1)]

        while stack:
            curr, parent = stack.pop()
            for nei, direction in edge[curr]:
                if nei != parent:
                    res += direction
                    stack.append((nei, curr))
        
        return res
    