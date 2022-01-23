# this problem can be simplified as seeing two people tranverse to the bottom right at same time
# this is actuall easy to understand too. consider n as steps, there will be total N*2-1 steps to complete the journey
# therefore we can easily pick two numbers as steps the two people tranverse to the right, then we automatically get how many steps down
# dp[i][p] = Math.max(dp[i][p], dp[i - 1][p - 1]); means compare both moving to the right (left) case

public int cherryPickup(int[][] grid) {
    int N = grid.length, M = (N << 1) - 1;
    int[][] dp = new int[N][N];
    dp[0][0] = grid[0][0];

    for (int n = 1; n < M; n++) {
		for (int i = N - 1; i >= 0; i--) {
			for (int p = N - 1; p >= 0; p--) {
				int j = n - i, q = n - p;

				if (j < 0 || j >= N || q < 0 || q >= N || grid[i][j] < 0 || grid[p][q] < 0) {
                    dp[i][p] = -1;
                    continue;
                 }

				 if (i > 0) dp[i][p] = Math.max(dp[i][p], dp[i - 1][p]);
				 if (p > 0) dp[i][p] = Math.max(dp[i][p], dp[i][p - 1]);
				 if (i > 0 && p > 0) dp[i][p] = Math.max(dp[i][p], dp[i - 1][p - 1]);

				 if (dp[i][p] >= 0) dp[i][p] += grid[i][j] + (i != p ? grid[p][q] : 0)
             }
		 }
    }

    return Math.max(dp[N - 1][N - 1], 0);

# recursion and memorization, key point is r1 + c1 = r2 + c2

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        M = len(grid)
        dp = [[[0 for i in range(M)] for j in range(M)] for k in range(M)]
        def helper(r1, c1, c2):
            r2 = r1+c1-c2
            if r1>=M or c1 >=M or r2 >=M or c2 >= M or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -sys.maxsize-1
            if dp[r1][c1][c2] != 0:
                return dp[r1][c1][c2]
            if r1 == M-1 and c1 == M-1:
                return grid[r1][c1]
            res = grid[r1][c1] + (grid[r2][c2] if r1 != r2 else 0)
            print(f"{r1},{c1} {r2},{c2} = {res}")
            res+= max(helper(r1+1,c1, c2),
                           helper(r1+1, c1, c2+1),
                           helper(r1,c1+1,c2),
                           helper(r1, c1+1, c2+1))
            dp[r1][c1][c2] = res


            return res
        return max(0, helper(0,0,0))
