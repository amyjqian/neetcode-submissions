class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            if l == mid or r == mid:
                return -1
            elif nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
                
        return -1
        