class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        dp = [-1000 for j in range(k*2)]
        res = 0
        for i in range(N):
            for j in range(k*2):
                if j % 2 == 0: # buy
                    dp[j] = max(dp[j], (dp[j-1] if j > 0 else 0) - prices[i])
                else: # sell
                    dp[j] = max(dp[j], (dp[j-1] if j > 0 else -1000) + prices[i])
                    res = max(res, dp[j])
        return res
                    
