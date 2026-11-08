from functools import cache
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # bottom up dp
        # stores sum and how many ways to get there 
        counts = {0: 1}
        for num in nums:
            nxt = defaultdict(int)
            for s, c in counts.items():
                nxt[s + num] += c 
                nxt[s - num] += c
            counts = nxt 
        return counts[target]

        # top down dp 
        # @cache
        # def ways(i, remaining):
        #     if i == len(nums):
        #         return 1 if remaining == 0 else 0 
        #     else:
        #         return ways(i + 1, remaining - nums[i]) + ways(i + 1, remaining + nums[i])
        
        # return ways(0, target)

        
        # recursion brute force 
        # if not nums:
        #     return 1 if target == 0 else 0
        
        # else:
        #     return self.findTargetSumWays(nums[1:], target - nums[0]) + self.findTargetSumWays(nums[1:], target + nums[0])
        