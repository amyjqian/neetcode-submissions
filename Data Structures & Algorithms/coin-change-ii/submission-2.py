class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # space optimized version
        dp = [0] * (amount + 1)
        dp[0] = 1 

        for coin in coins:
            for a in range(coin, amount + 1):
                if amount - coin >= 0:
                    dp[a] += dp[a - coin]
        return dp[amount]
        
        # find all possible solutions: 
        # n = len(coins)
        # coins.sort()
        # # dp represents the number of ways to make amount with coins[i:] 
        # # dp = (n + 1) * (amount + 1) matrix where dp[i][a] = make a with coins[i:]
        # dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # for i in range(n + 1):
        #     dp[i][0] = 1 
        
        # for i in range(n - 1, -1 , -1):
        #     for a in range(amount + 1):
        #         if a - coins[i] >= 0: # solution either contains coins or does not contain coins 
        #             dp[i][a] = dp[i + 1][a] + dp[i][a - coins[i]]
        
        # return dp[0][amount]

        # dp = [amount + 1] * (amount + 1)

        # dp[0] = 0

        # for a in range(1, amount + 1):
        #     for coin in coins:
        #         dp[a] = min(dp[a], 1 + dp[a - coin])
        
        # return dp[amount] if dp[amount] != amount + 1 else -1

        