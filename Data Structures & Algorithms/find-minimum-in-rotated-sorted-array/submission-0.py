class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
            # cases l < mid  and mid < r:
                # go left, r = mid - 1
            # case l < mid and mid > r:
                # go right, l = mid + 1
            # case l > mid and mid < r:
                # go left, r = mid - 1
            # case l > mid and mid > r:
                # not possible????


        

        