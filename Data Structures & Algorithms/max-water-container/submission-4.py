class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = (r - l) * min(heights[l], heights[r])
        while l < r:
            if heights[l] <= heights[r]:
                l += 1            
            elif heights[l] > heights[r]:
                r -= 1
            area = max(area, (r-l) * min(heights[l], heights[r]))
            # print(f"l: {l}, heights[l]: {heights[l]}")
            # print(f"r: {r}, heights[r]: {heights[r]}")
        return max(area, (r-l) * min(heights[l], heights[r]))

        