class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Time complexity: O(N + E): N is the number of rooms, E is the total number of keys
        Space complexity: O(N)
        """
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]

        while stack:
            node = stack.pop()
            for nei in rooms[node]:
                if not seen[nei]:
                    seen[nei] = True
                    stack.append(nei)
        """
        all() function returns True if all items in an 
        iterable are true, otherwise return false
        """
        return all(seen)