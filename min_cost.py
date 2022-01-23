class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        i = 0
        while i < len(s)-1:
            current = cost[i]
            while i < len(s)-1 and s[i] == s[i+1]:
                res += min(current, cost[i+1])
                current = max(current, cost[i+1])
                i += 1
            i+=1
        return res
