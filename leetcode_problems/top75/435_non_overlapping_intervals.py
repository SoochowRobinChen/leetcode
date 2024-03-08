class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the list by ascending order in end
        intervals = sorted(intervals, key=lambda x: (x[1], x[0]))
        result = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                result += 1
            else:
                end = intervals[i][1]
        
        return result
    