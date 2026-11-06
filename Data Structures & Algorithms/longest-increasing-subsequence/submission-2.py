class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # recursion 
        dp = [1] * (len(nums) + 1)

        dp[0] = 1 

        for i in range(1, len(nums)):
            ans = 1
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    ans = max(ans, 1 + dp[j])
            dp[i] = ans
        return max(dp)


        