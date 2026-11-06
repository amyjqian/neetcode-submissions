from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hashmap and heap? 
        # for each num encountered check for n-1 in hashmap
        # return max value in hashmap
        numSet = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
                