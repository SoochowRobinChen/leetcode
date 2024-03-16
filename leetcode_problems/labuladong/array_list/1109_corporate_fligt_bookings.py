class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)

        for booking in bookings:
            start = booking[0]
            end = booking[1]
            val = booking[2]

            diff[start] += val

            if end + 1 <= n:
                diff[end + 1] -= val
        
        res = [diff[1]]

        for i in range(2, n + 1):
            res.append(res[-1] + diff[i])

        return res