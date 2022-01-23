# common solution: encoding on board to save space
# <2        1->0     2
# 2,3       1->1     1
# >3        1->0     2
# 3         0->1     3
class Solution(object):
    def gameOfLife(self, board):
        if not board or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, ele in enumerate(row):
                count = 0
                for a in xrange(max(0, i - 1), min(i + 2, m)):
                    for b in xrange(max(0, j - 1), min(j + 2, n)):
                        if (a, b) != (i, j) and 1 <= board[a][b] <= 2:
                            count += 1
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1


# infinite board question: save live cells only for counter
def gameOfLifeInfinite(self, live):
    ctr = collections.Counter((I, J)
                              for i, j in live
                              for I in range(i-1, i+2)
                              for J in range(j-1, j+2)
                              if I != i or J != j)
    return {ij
            for ij in ctr
            if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}
def gameOfLife(self, board):
    live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
    live = self.gameOfLifeInfinite(live)
    for i, row in enumerate(board):
        for j in range(len(row)):
            row[j] = int((i, j) in live)
