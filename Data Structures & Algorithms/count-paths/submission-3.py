import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)

        # dp = [0] * n
        # dp[0] = 1
        # for _ in range(m):
        #     for j in range(1, n):
        #         dp[j] += dp[j-1]

        # return dp[-1]

        # dp = [[0 for _ in range(n)] for _ in range(m)] 
        # dp[0][0] = 1

        # for i in range(m):
        #     for j in range(n):
        #         if i != 0 :
        #             dp[i][j] += dp[i-1][j]
        #         if j != 0:
        #             dp[i][j] += dp[i][j-1]
        
        # return dp[m-1][n-1]
        