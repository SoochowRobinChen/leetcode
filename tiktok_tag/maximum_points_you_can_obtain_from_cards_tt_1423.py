class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_sum = 0
        smallest = float('inf')
        total_sum = sum(cardPoints)

        left, right = 0, 0
        if k == len(cardPoints):
            return total_sum

        while right < len(cardPoints):
            window_sum += cardPoints[right]
            right += 1

            while left < right and right - left >= len(cardPoints) - k:
                smallest = min(smallest, window_sum)
                window_sum -= cardPoints[left]
                left += 1
            
        
        return total_sum - smallest 