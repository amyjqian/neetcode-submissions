class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # holding stock: 
            # sell (add price and skip to next day)
            # skip the day 
            # take max 
        # not holding stock:
            # buy stock (subtract price and skip to next day)
            # skip the day 
            # take min 
        dp = [[0] * 2 for _ in range(len(prices) + 1)] # dp[i][1] is True if you can buy and false otherwise 

        for i in range(len(prices) - 1, -1, -1):
            buy = dp[i + 1][0] - prices[i] 
            cooldown = dp[i + 1][1]
            dp[i][1] = max(buy, cooldown)

            sell = dp[i + 2][1] + prices[i] if i + 2 < len(prices) else prices[i]
            cooldown = dp[i + 1][0]
            dp[i][0] = max(sell, cooldown)
        
        return dp[0][1]






        