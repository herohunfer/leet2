class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = n < 0
        if n == 0:
            return 1
        n = abs(n)
        base = x
        res = 1
        while n >0:
            n, mod = divmod(n,2)
            res *= mod * base if mod > 0 else 1
            base *= base
        if sign:
            return 1/res
        else:
            return res

            
