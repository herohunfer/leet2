class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        stack = []
        stack += [(k, 0) for k in range(m)]
        stack += [(k, n-1) for k in range(m)]
        stack += [(0, k) for k in range(n)]
        stack += [(m-1, k) for k in range(n)]

        while stack:
            i, j = stack.pop()
            if 0 <= i < m and 0<=j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                stack += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

        board[:] = [['XO'[c=='S'] for c in 'S' for c in row] for row in board]
