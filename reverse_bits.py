class Solution:
    def reverseBits(self, n: int) -> int:
        i = 0
        j = 31
        while i < j:
            bit = n & (1 << i)
            if n& (1<<j):
                n |= 1 << i
            else:
                n &= ~(1<<i)
            if bit:
                n |= 1<< j
            else:
                n &= ~(1<<j)
            i += 1
            j -= 1
        return n
