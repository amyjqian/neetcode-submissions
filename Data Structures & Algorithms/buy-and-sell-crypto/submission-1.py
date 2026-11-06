class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # d,p problem
        l, r = 0, 0
        profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                curr = (prices[r] - prices[l])
                profit = max(profit, curr)
                r += 1
            else:
                curr = (prices[r] - prices[l])
                profit = max(profit, curr)
                l = r
                r += 1
        return profit
