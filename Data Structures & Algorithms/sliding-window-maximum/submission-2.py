import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        l, r = 0, k
        ans = []
        while r < len(nums):
            while heap[0][1] < l:             # clean up first, as many as needed
                heapq.heappop(heap)
            ans.append(-heap[0][0])           # now the top is in the window
            heapq.heappush(heap, (-nums[r], r))
            l += 1
            r += 1
        
        while heap[0][1] < l:                 # record the last window
            heapq.heappop(heap)
        ans.append(-heap[0][0])
        
        return ans
        
        
        # brute force
        # ans = []
        # l, r = 0, k - 1
        # while r < len(nums):
        #     ans.append(max(nums[l:r + 1]))
        #     l += 1
        #     r += 1
        # return ans

        