class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # iterate the trips to find max distance
        max_distance = 0
        for t in trips:
            max_distance = max(max_distance, t[2])
        
        diff = [0] * (max_distance + 1)

        for t in trips:
            diff[t[1]] += t[0]
            diff[t[2]] -= t[0]

        res = [diff[0]]

        for i in range(1, len(diff)):
            res.append(res[-1] + diff[i])
        
        for val in res:
            if val > capacity:
                return False
        
        return True
    