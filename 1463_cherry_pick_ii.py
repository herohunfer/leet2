class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        res = 0
        acts = [(-1, -1), (-1, 0), (-1, 1), (0,-1), (0,0), (0,1), (1,-1), (1,0),(1,1)]
        M, N = len(grid[0]), len(grid)
        m1, m2 = {(0, M-1): grid[0][0] + grid[0][M-1]}, {}
        q = [(0, M-1)]

        newq = []
        for row in range(1, N):
            while q:
                pos1, pos2 = q.pop()
                # print(f"get new pos1={pos1} pos2={pos2}")
                for act in acts:
                    if 0 <= pos1 + act[0] < M and 0 <= pos2 + act[1] < M:
                        newpos1 = min(pos1 + act[0], pos2 + act[1])
                        newpos2 = max(pos1 + act[0], pos2 + act[1])
                        # print(f"pos1={pos1} pos2={pos2} newpos1={newpos1} newpos2={newpos2} row={row}")
                        val = m1[(pos1, pos2)] + grid[row][newpos1] + (grid[row][newpos2] if newpos1 != newpos2 else 0)
                        if (newpos1, newpos2) in m2:
                            m2[(newpos1, newpos2)] = max(m2[(newpos1, newpos2)], val)
                        else:
                            m2[(newpos1, newpos2)] = val
                            newq.append((newpos1, newpos2))
            q = newq
            m1 = m2
            m2 = {}
            newq = []
            # print(f"q={q} m1={m1}")
        return max(m1.values())
