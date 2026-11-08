from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def ways(i, remaining):
            if i == len(nums):
                return 1 if remaining == 0 else 0 
            else:
                return ways(i + 1, remaining - nums[i]) + ways(i + 1, remaining + nums[i])
        
        return ways(0, target)

        
        # recursion brute force 
        # if not nums:
        #     return 1 if target == 0 else 0
        
        # else:
        #     return self.findTargetSumWays(nums[1:], target - nums[0]) + self.findTargetSumWays(nums[1:], target + nums[0])
        