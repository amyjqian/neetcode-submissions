class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        best = 0
        for i in range(n + 1):
            if i == n:
                height = 0
            else:
                height = heights[i]
            while stack and heights[stack[-1]] >= height:
                top_index = stack.pop()
                bar_height = heights[top_index]
                left = stack[-1] if stack else -1 
                width = i - left - 1
                best = max(best, bar_height * width)
            stack.append(i)
        return best
        







        