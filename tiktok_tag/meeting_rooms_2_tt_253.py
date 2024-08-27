class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        endpoints = []

        for start, end in intervals:
            endpoints.append((start, 1))
            endpoints.append((end, -1))
            # avoid overcounting
        
        endpoints.sort()
        res = 0
        curr = 0

        for _, delta in endpoints:
            curr += delta
            res = max(res, curr)
        
        return res 