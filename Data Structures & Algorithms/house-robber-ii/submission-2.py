class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums)
        
        rob1, rob2 = 0, 0
        for num in nums[:-1]:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp 
        ans1 = max(rob1, rob2)
        rob3, rob4 = 0, 0
        for num in nums[1:]:
            temp = max(rob3 + num, rob4)
            rob3 = rob4
            rob4 = temp 
        ans2 = max(rob3, rob4)
        return max(ans1, ans2)
    




        