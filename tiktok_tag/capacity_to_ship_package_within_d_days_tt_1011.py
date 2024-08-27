class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        def days_need(workload):
            days = 0
            i = 0

            while i < len(weights):
                capacity = workload
                while i < len(weights):
                    if weights[i] > capacity:
                        break
                    else:
                        capacity -= weights[i]
                        i += 1
                days += 1
            
            return days 
        

        while left < right:
            mid = left + (right - left) // 2
            curr_days = days_need(mid)
            if curr_days <= days:
                right = mid
            else:
                left = mid + 1
        
        return left 