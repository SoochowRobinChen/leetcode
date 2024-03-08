class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[1], x[0]))

        endpoint = points[0][1]
        num = 1

        for i in range(1, len(points)):
            if points[i][0] > endpoint:
                num += 1
                endpoint = points[i][1]
        
        return num
    