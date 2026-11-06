class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # at each index stay or add 
        # 
        if len(cost) == 2:
            return min(cost[0], cost[1])

        dp = [0] * (len(cost) + 1)
        
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        return dp[len(cost)]

        # if len(cost) == 1:
        #     return cost[0]
        
        # if len(cost) == 2:
        #     return min(cost)
        
        # if len(cost) == 3:
        #     return min(cost[0] + cost[2], cost[1])
        
        # else:
        #     return min(cost[-1] + self.minCostClimbingStairs(cost[:-1]), cost[-2] + self.minCostClimbingStairs(cost[:-2]))
            

        


        