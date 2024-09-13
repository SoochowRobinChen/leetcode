class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # dp[i] = max(dp[i-k .. i-1]) + nums[i]

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        deq = deque()
        deq.append(0)


        for i in range(1, n):
            if deq[0] < i - k:
                deq.popleft()
            
            dp[i] = dp[deq[0]] + nums[i]

            while deq and dp[deq[-1]] < dp[i]:
                deq.pop()
            
            deq.append(i)

        return dp[-1]