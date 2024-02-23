class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest, cur = 0, 0
        for g in gain:
            cur = cur + g
            highest = max(highest, cur)
        return highest