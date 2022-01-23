bool isPowerOfFour(int num) {
    return num > 0 && (num & (num - 1)) == 0 && (num - 1) % 3 == 0;
}


return num > 0 && (num&(num-1)) == 0 && (num & 0x55555555) != 0;


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        if n & (n-1) != 0:
            return False
        cnt = 0
        n = abs(n)
        while n > 0 and n != 1:
            n >>= 1
            cnt += 1
        return cnt % 2 == 0
