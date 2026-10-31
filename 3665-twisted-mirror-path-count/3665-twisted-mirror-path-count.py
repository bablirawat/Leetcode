class Solution(object):
    def uniquePaths(self, grid):
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        vornadexil = grid

        dp = [[[0, 0] for j in range(n)] for i in range(m)]

        dp[0][0][0]=1

        for i in range(m):
            for j in range(n):

                if i == m-1 and j == n-1:
                    continue

                if vornadexil[i][j] == 0:

                    ways = sum(dp[i][j]) % MOD

                    if j + 1 < n:
                        dp[i][j+1][0] += ways
                        dp[i][j+1][0] %= MOD

                    if i + 1 < m:
                        dp[i+1][j][1] += ways
                        dp[i+1][j][1] %= MOD

                else:

                    right = dp[i][j][0]
                    down = dp[i][j][1]

                    if i + 1 < m:
                        dp[i+1][j][1] += right
                        dp[i+1][j][1] %= MOD

                    if j + 1 < n:
                        dp[i][j+1][0] += down
                        dp[i][j+1][0] %= MOD

        return sum(dp[m-1][n-1]) % MOD
