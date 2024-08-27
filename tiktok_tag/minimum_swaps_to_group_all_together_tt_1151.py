class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        cnt_one = 0
        window_ones = 0

        left, right = 0, 0

        while right < len(data):
            cnt_one += data[right]
            right += 1

            if right - left > ones:
                cnt_one -= data[left]
                left += 1
            
            window_ones = max(window_ones, cnt_one)
        
        return ones - window_ones