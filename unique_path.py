class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        S = [[0 for i in range(m)] for j in range(n)]
        for j in range(n):
            for i in range(m):
                if i == 0 and j ==0:
                    S[j][i] = 1
                else:
                    S[j][i] = (S[j-1][i] if 1<=j else 0) + (S[j][i-1] if 1<=i else 0)
        print(S)
        return S[-1][-1]

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(7,3))
