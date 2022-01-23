class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow



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
            res *= base if mod > 0 else 1
            base *= base
        if sign:
            return 1/res
        else:
            return res
