class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # modify in place 
        # we know that number we want is target - numbers[i]
        # numbers increase. x can not be smaller than current number 
        l, r = 0, len(numbers) - 1
        while (1):
            while numbers[l] + numbers[r] > target:
                r -= 1
            while numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]



        
        
        # o(n) memory solution
        # seen = {}

        # for i in range(len(numbers)):
        #     x = target - numbers[i]
        #     if x in seen:
        #         return [seen[x], i + 1]
        #     else:
        #         seen[numbers[i]] = i + 1
        