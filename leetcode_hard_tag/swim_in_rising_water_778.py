class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        min_heap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited.add((0, 0))

        while min_heap:
            t, r, c = heappop(min_heap)
            

            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or neiR >= N or neiC >= N or (neiR, neiC) in visited):
                    continue
                visited.add((neiR, neiC))
                heappush(min_heap, (max(t, grid[neiR][neiC]), neiR, neiC))