class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in dict:
                return [dict[x], i]
            dict[nums[i]] = i
        