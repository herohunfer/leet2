class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        res, res2 = matrix[0], [sys.maxsize] * n
        for i in range(1, n):
            row = matrix[i]
            for j in range(len(res2)):
                res2[j] = row[j]+min(res[j], res[j-1] if j else sys.maxsize, res[j+1] if j < n-1 else sys.maxsize)
            res, res2 = res2, [sys.maxsize] * n
        return min(res)
