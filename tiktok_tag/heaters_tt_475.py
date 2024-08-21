class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()

        def can_cover_all(radius):
            i, j = 0, 0

            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) > radius:
                    j += 1
                else:
                    i += 1
            
            return i == len(houses)
        

        # binary search
        left, right = 0, max(houses[-1], heaters[-1])

        while left < right:
            mid = left + (right - left) // 2
            if can_cover_all(mid):
                right = mid
            else:
                left = mid + 1
        
        return left 