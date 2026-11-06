class Solution:
    def trap(self, height: List[int]) -> int:
        # find area - two pointers that are the highest in a subregion
        # hashmap
        # at each index store the water it can hold 
        # start at two pointers at beginning. 
        # increment R. if encounter a value that is greater than L, stop
        # if smaller than L, add (index: water held)
        # calculate area
        # subtract 
        if len(height) < 3:
            return 0
        
        before = [0] * len(height)
        biggest = 0
        for i in range(len(height)):
            biggest = max(biggest, height[i])
            before[i] = biggest
        
        after = [0] * len(height)
        biggest = 0
        for i in range(len(height) - 1, -1, -1):
            biggest = max(biggest, height[i])
            after[i] = biggest
        
        running_total = 0

        for i in range(len(height)):
            running_total += (min(before[i], after[i]) - height[i])
        return running_total
            

