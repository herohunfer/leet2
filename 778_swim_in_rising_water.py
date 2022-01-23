# once the node is processed, no need to process it again
# and also once reaches x==y==N-1 we can immediately return

class Solution:
    def swimInWater(self, grid):
        N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        while True:
            T, x, y = heapq.heappop(pq)
            res = max(res, T)
            if x == y == N - 1:
                return res
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
                    seen.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))



import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h = []
        heappush(h, (grid[0][0], 0,0))
        M = len(grid)
        m = [[M*M for i in range(M)] for j in range(M)]
        m[0][0] = grid[0][0]
        actions = [(0,1), (1,0), (-1,0), (0, -1)]
        while h:
            _, i,j = heappop(h)
            for ai,aj in actions:
                newi = i + ai
                newj = j + aj
                if 0<=newi<M and 0<=newj<M:
                    if m[newi][newj] == M*M:
                        heappush(h, (grid[newi][newj], newi,newj))
                    m[newi][newj] = min(m[newi][newj], max(m[i][j], grid[newi][newj]))
        # print(m)
        return m[-1][-1]
