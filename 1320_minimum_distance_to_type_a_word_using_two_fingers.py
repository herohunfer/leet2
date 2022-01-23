import sys
from functools import cache


# switching hands are key
def minimumDistance(self, A):
    def d(a, b):
        return abs(a / 6 - b / 6) + abs(a % 6 - b % 6)
    A = [ord(c) - 65 for c in A]
    dp = [0] * 26
    for b, c in zip(A, A[1:]):
        dp[b] = max(dp[a] + d(b, c) - d(a, c) for a in xrange(26))
    return sum(d(b, c) for b, c in zip(A, A[1:])) - max(dp)


class Solution:
    def minimumDistance(self, word: str) -> int:
        @cache
        def d(i,j):
            return i and abs(i//6 - j//6) + abs(i%6-j%6)

        dp, dp2 = {(0,0):0}, {}
        for c in (ord(c)+1 for c in word):
            for a,b in dp:
                dp2[a,c] = min(dp2.get((a,c), 3000), dp[a,b] + d(b,c))
                dp2[c,b] = min(dp2.get((c,b), 3000), dp[a,b] + d(a,c))
            dp, dp2 = dp2, {}
        return min(dp.values())




class Solution:
    def minimumDistance(self, word: str) -> int:
        @cache
        def helper(i, j):
            if i == 26 or j == 26:
                return 0
            return abs(i // 6 - j // 6) + abs(i%6-j%6)
        m = [[[sys.maxsize for k in range(27)] for j in range(27)] for i in range(len(word)+1)]
        m[0][26][26] = 0
        res = [[0,26,26]]
        visited = set((0,26,26))
        pos = 0
        best = sys.maxsize
        while pos < len(res):
            i,j,k = res[pos]
            if i == len(word):
                best = min(best, m[i][j][k])
            else:
                val = ord(word[i])-ord('A')
                temp = [i+1, val, k]
                m[temp[0]][temp[1]][temp[2]] = min(m[temp[0]][temp[1]][temp[2]], m[i][j][k] + helper(j, val))
                if tuple(temp) not in visited:
                    visited.add(tuple(temp))
                    res.append(temp)
                temp = [i+1, j, val]
                m[temp[0]][temp[1]][temp[2]] = min(m[temp[0]][temp[1]][temp[2]], m[i][j][k] + helper(k, val))
                if tuple(temp) not in visited:
                    visited.add(tuple(temp))
                    res.append(temp)
            pos += 1
        print(len(res))
        print(m)
        return best




# class Solution:
#     def minimumDistance(self, word: str) -> int:
#         def helper(i, j):
#             if i == 26 or j == 26:
#                 return 0
#             return abs(i // 6 - j // 6) + abs(i%6-j%6)
#         m = [[[sys.maxsize for k in range(27)] for j in range(27)] for i in range(len(word)+1)]
#         m[0][26][26] = 0
#         for i in range(len(word)):
#             for j in range(27):
#                 for k in range(27):
#                     m[i+1][ord(word[i])-ord('A')][k] = min(m[i+1][ord(word[i])-ord('A')][k],
#                                                            m[i][j][k] + helper(j, ord(word[i])-ord('A')))
#                     m[i+1][j][ord(word[i])-ord('A')] = min(m[i+1][j][ord(word[i])-ord('A')],
#                                                            m[i][j][k] + helper(k, ord(word[i])-ord('A')))
#         print(m)
#         return min(m[-1][j][k] for j in range(27) for k in range(27))

if __name__ == "__main__":
    s = Solution()
    print(s.minimumDistance("YEAR"))
