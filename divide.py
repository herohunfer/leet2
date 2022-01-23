class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = dividend * divisor < 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend == 0:
            return 0
        res = 0
        current = divisor
        pos = 0
        while dividend >= current:
            current <<= 1
            pos+= 1
        current >>= 1
        print(f"pos={pos} current={current}")
        for i in range(pos):
            if dividend >= current:
                dividend -= current
                res += 1
            res <<= 1
            current >>= 1
            print(f"i={i} dividend={dividend} res={res} current={current}")
        res =  -(res >> 1) if neg else (res >> 1)
        print(res)
        return res if -(2**31) <= res <= (2**31-1) else (2**31-1)

if __name__ == "__main__":
    s = Solution()
    print(s.divide(-2147483648, -1))
