class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[-100000 for j in range(4)] for i in range(N)]
        res = 0
        currentMin = 100000
        prevMax = 0
        prevBuy2 = -100000
        for i in range(N):
            dp[i][0] = -prices[i]
            currentMin = min(currentMin, prices[i])
            dp[i][1] = max(0, prices[i]-currentMin)
            res = max(res, dp[i][1])
            prevMax = max(prevMax, dp[i][1])
            dp[i][2] = prevMax - prices[i]
            prevBuy2 = max(prevBuy2, dp[i][2])
            dp[i][3] =  prices[i] + prevBuy2
            res = max(res, dp[i][3])
        return res
