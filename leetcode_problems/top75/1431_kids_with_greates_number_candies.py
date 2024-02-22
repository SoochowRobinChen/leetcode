class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # use one variable to store max value
        maxVal = max(candies)
        # iterate give True | False
        return [c + extraCandies >= maxVal for c in candies]