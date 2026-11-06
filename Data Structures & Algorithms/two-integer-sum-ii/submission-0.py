class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(numbers)):
            x = target - numbers[i]
            if x in seen:
                return [seen[x], i + 1]
            else:
                seen[numbers[i]] = i + 1
        