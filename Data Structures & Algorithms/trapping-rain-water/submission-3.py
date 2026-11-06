class Solution:
    def trap(self, height: List[int]) -> int:
        # left and right array 
        # left array stores distance to biggest bar
        # right array stores distanc to biggest bar 
        # ans = min(left, right)
        left = [0] * len(height)
        right = [0] * len(height)

        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(right[i + 1], height[i + 1])
        
        ans = [0] * len(height)
        running_total = 0
        for i in range(len(height)):
            running_total += max(0, min(left[i], right[i]) - height[i])

        return running_total





        