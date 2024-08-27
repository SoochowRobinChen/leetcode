class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        对比1514题，这一题就用了visited() set 来记录已经访问过的点
        来确保不走回头路
        """

        rows, cols = len(heights), len(heights[0])

        visited = set()
        min_heap = [[0, 0, 0]]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while min_heap:
            diff, r, c = heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) == (rows - 1, cols - 1):
                return diff
            for nr, nc in directions:
                rr, cc = r + nr, c + nc
                if rr < 0 or cc < 0 or rr >= rows or cc >= cols or (rr, cc) in visited:
                    continue
                
                new_diff = max(diff, abs(heights[rr][cc] - heights[r][c]))
                heappush(min_heap, [new_diff, rr, cc])