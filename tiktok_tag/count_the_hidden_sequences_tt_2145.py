class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        next_minimum, next_maximum = 0, 0
        current = 0

        for num in differences:
            current += num
            next_minimum = min(current, next_minimum)
            next_maximum = max(current, next_maximum)
        
        return max((upper - lower) - (next_maximum - next_minimum) + 1, 0)