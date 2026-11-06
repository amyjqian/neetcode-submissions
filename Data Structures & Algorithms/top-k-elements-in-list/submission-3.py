import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap? 
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        heap = [(-value, key) for key, value in freq.items()]

        heapq.heapify(heap)

        ans = []
        for i in range(k):
            val = heapq.heappop(heap)
            ans.append(val[1])
        return ans

            
        