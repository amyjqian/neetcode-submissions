from collections import defaultdict
import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # hashmap for each s and t
        # find first index it could possibly be
        # then increment R. 
        # if solution found, increment L until solution not true

        freq_t = defaultdict(int)
        freq_set = set()
        for i in range(len(t)):
            freq_t[t[i]] += 1
            freq_set.add(t[i])
        have = len(freq_set)
        
        freq_s = defaultdict(int)
        l = 0
        need = 0
        max_len = -1
        ans = ""

        for r in range(len(s)):
            freq_s[s[r]] += 1
            if s[r] in freq_set and freq_s[s[r]] == freq_t[s[r]]:
                need += 1
            
            while need == have:
                if max_len == -1 or (r - l) + 1 < max_len:
                    max_len = r - l + 1
                    ans = s[l: r + 1]
                freq_s[s[l]] -= 1
                if s[l] in freq_set and freq_s[s[l]] < freq_t[s[l]]:
                    need -= 1
                l += 1
        return ans
