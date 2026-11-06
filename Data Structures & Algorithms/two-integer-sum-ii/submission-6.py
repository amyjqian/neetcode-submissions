class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sliding window 
        # l, r 
        l, r = 0, len(numbers) - 1
        while l < r:
            # print(f"l: {l}")
            # print(f"r: {r}")
            # print(f"answer: {numbers[l] + numbers[r]}")
            if (numbers[l] + numbers[r]) == target:
                return [l + 1, r + 1]

            if (numbers[l] + numbers[r]) > target:
                # print("here")
                r -= 1
            elif (numbers[l] + numbers[r]) < target:
                # print("here")
                l += 1
        return [l + 1, r + 1]
            


        