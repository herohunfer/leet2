class Solution:
    def regionsBySlashes(self, grid) -> int:
        n = len(grid)
        grids = [[0 for i in range(3*n)] for j in range(3*n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '\\':
                    grids[3*i][3*j] = 1
                    grids[3*i+1][3*j+1] = 1
                    grids[3*i+2][3*j+2] = 1
                elif grid[i][j] == '/':
                    grids[3*i][3*j+2] = 1
                    grids[3*i+1][3*j+1] = 1
                    grids[3*i+2][3*j] = 1
        res = 0
        n *= 3
        print(grids)
        for i in range(n):
            for j in range(n):
                if grids[i][j] == 0:
                    res += 1
                    q = [(i,j)]
                    while q:
                        ci, cj = q.pop()
                        if ci > 0 and not grids[ci-1][cj]:
                            grids[ci-1][cj] = 1
                            q.append((ci-1,cj))
                        if ci < n-1 and not grids[ci+1][cj]:
                            grids[ci+1][cj] = 1
                            q.append((ci+1, cj))
                        if cj > 0 and not grids[ci][cj-1]:
                            grids[ci][cj-1] = 1
                            q.append((ci, cj-1))
                        if cj < n-1 and not grids[ci][cj+1]:
                            grids[ci][cj+1] = 1
                            q.append((ci, cj+1))
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.regionsBySlashes(["/\\","\\/"]))
