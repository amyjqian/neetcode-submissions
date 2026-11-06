class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # run two sums on three sums 
        nums.sort()

        result = []
        for i in range(len(nums)):
            x = -nums[i]
            print(f"loop: {nums[i]}")
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ans = self.twoSums(nums[i + 1:], x)
            if ans:
                for j in range(len(ans)):
                    ans[j].append(nums[i])
                    result.append(ans[j])
        return result

    
    def twoSums(self, lst, target):
        ans = []
        l, r = 0, len(lst) - 1
        while l < r:
            while l < r and lst[l] + lst[r] > target:
                r -= 1
            while l < r and lst[l] + lst[r] < target:
                l += 1
            if lst[l] + lst[r] == target and l != r:
                ans.append([lst[l],lst[r]])
                l += 1
                r -= 1
                while l < r and lst[l] == lst[l-1]:
                    l += 1
        return ans

        