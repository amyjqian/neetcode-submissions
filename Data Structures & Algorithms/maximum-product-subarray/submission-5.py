class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane algorithm 
        res = nums[0]
        currMax, currMin = 1, 1
        for num in nums:
            currMax, currMin = max(currMax * num, currMin * num, num), min(currMax * num, currMin * num, num)
            res = max(res, currMax)
        return res




        # res = nums[0]

        # for i in range(len(nums)):
        #     curr = nums[i]
        #     res = max(res, curr)
        #     for j in range(i + 1, len(nums)):
        #         curr *= nums[j]
        #         res = max(res, curr)
        # return res 