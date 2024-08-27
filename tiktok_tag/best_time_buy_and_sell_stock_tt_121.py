class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(days)]

        # init
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, days):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(-prices[i], dp[i-1][1])


        return dp[-1][0]