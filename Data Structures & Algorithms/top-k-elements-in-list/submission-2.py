from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        heap_by_values = [(-value, key) for key, value in hashmap.items()]
        heapq.heapify(heap_by_values)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap_by_values)[1])
        return ans
        