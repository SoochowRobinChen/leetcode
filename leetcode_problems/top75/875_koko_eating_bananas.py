class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles: return 0

        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if self.get_hours(piles, mid) <= h:
                right = mid
            else:
                left = mid + 1
        
        return left

    def get_hours(self, piles, speed):
        hours = 0
        for pile in piles:
            hours += pile // speed
            if pile % speed:
                hours += 1
        
        return hours