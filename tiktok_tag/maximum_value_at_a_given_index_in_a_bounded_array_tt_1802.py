class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def get_sum_in_range(peak, length):
            total_sum = 0
            if length > peak:
                total_sum += (1 + peak) * peak / 2
                total_sum += (length - peak)
            else:
                minimum = peak - length + 1
                total_sum += (minimum + peak) * length / 2
            
            return total_sum

        
        # use binary search 
        left, right = 1, maxSum
        ans = 1
        while left <= right:
            mid = left + (right - left) // 2
            curr_sum = get_sum_in_range(mid, index + 1) + get_sum_in_range(mid, n - index) - mid
            if curr_sum <= maxSum:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        
        return ans 