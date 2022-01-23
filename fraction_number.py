class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        whole = numerator // denominator
        res = str(whole)
        numerator -= whole * denominator
        if numerator == 0:
            return res
        else:
            res += "."
        fraction = ""
        cache = set()
        while True:
            numerator *= 10
            current = numerator // denominator
            numerator = numerator % denominator
            fraction += str(current)
            if numerator == 0:
                return res + fraction
            else:
                if numerator in cache:
                    for i in range(1, len(fraction)//2+1):
                        if fraction[-i:] == fraction[-2*i:-i]:
                            return res + fraction[:-2*i] + f"({fraction[-i:]})"
                elif current > 0:
                    cache.add(numerator)
