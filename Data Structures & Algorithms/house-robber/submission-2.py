class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)

        dp = [0] * (len(nums) + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[len(nums) - 1]

        # slow recursive solution
        # if len(nums) == 1:
        #     return nums[0]
        
        # if len(nums) == 2:
        #     return max(nums)
        
        # if len(nums) == 3:
        #     return max(nums[0] + nums[2], nums[1])
        
        # else:
        #     # print(f"nums[-2]: {nums[-2:]}")
        #     # print(f"nums[-3]: {nums[-3:]}")
        #     return max(nums[-1] + self.rob(nums[:-2]), nums[-2] + self.rob(nums[:-3]))
        

        