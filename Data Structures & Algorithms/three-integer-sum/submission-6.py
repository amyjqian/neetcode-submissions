class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def twosum(lst, target):
            l, r = 0, len(lst) - 1
            ans = []
            while l < r:
                if lst[l] + lst[r] == target:
                    ans.append([lst[l], lst[r]])
                    l += 1
                    r -= 1
                    while l < r and lst[l] == lst[l - 1]:
                        l += 1
                elif lst[l] + lst[r] < target:
                    l += 1
                elif lst[l] + lst[r] > target:
                    r -= 1
            # print(f"ans in helper: {ans}")
            return ans

        # print(nums)
        i = 0
        ans = []
        prev = None
        while i < len(nums):
            if prev is None or prev != nums[i]:
                target = -nums[i] 
                res = twosum(nums[i + 1:], target)
                # print(f"res: {res}")
                if res != []:
                    for r in res:
                        ans.append([nums[i]] + r)
                prev = nums[i]
            i += 1
        # print(ans)
        return ans



        