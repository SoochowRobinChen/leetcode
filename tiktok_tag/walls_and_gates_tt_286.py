class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        EMPTY = 2147483647
        GATE = 0
        DIRECTIONS = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        row, col = len(rooms), len(rooms[0])

        #  start from Gate
        q = deque()
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == GATE:
                    q.append((i, j))
        
        while q:
            x, y = q.popleft()
            for dirx, diry in DIRECTIONS:
                nx, ny = dirx + x, diry + y
                if nx < 0 or ny < 0 or nx >= row or ny >= col or rooms[nx][ny] != EMPTY:
                    continue
                
                rooms[nx][ny] = rooms[x][y] + 1

                q.append((nx, ny))
                