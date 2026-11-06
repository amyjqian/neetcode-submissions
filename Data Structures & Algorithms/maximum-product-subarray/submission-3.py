class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane algorithm 
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num 
            curMax = max(num, num * curMax, num * curMin)
            curMin = min(num, tmp, num * curMin)
            res = max(res, curMax)
        return res 



        # res = nums[0]

        # for i in range(len(nums)):
        #     curr = nums[i]
        #     res = max(res, curr)
        #     for j in range(i + 1, len(nums)):
        #         curr *= nums[j]
        #         res = max(res, curr)
        # return res 