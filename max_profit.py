class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMin = 10000
        res = 0
        for price in prices:
            res = max(res, price-currentMin)
            currentMin = min(currentMin, price)
        return res
