class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            forward[i] = nums[i + 1] * forward[i + 1]
        backwards = [1] * len(nums)
        for i in range(1, len(nums)):
            backwards[i] = backwards[i - 1] * nums[i - 1]
        for i in range(len(nums)):
            nums[i] = forward[i] * backwards[i]
        return nums

        
        