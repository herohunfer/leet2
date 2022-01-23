class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if row == n or column == n:
            return 0.0
        if k == 0:
            return 1.0
        res = 0
        q = {(row, column): 1}
        qnew = {}
        d = [(1,2), (2,1), (2,-1), (1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
        cnt = 0
        for _ in range(k):
            cnt = 0
            for current in q:
                for i,j in d:
                    if 0 <= current[0] + i < n and 0 <= current[1] +j < n:
                        if (current[0]+i, current[1]+j) in qnew:
                            qnew[(current[0]+i, current[1]+j)] += q[current]
                        else:
                            qnew[(current[0]+i, current[1]+j)] = q[current]
            q = qnew
            qnew = {}
        return sum(q.values())/(8**k)
