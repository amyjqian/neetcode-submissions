from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hashmap stores {char: freq, index}
        # for each character encountered increment hashmap 
        # remove as needed 

        # stores the index 
        # for each index, 
        freq = defaultdict(int)
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            maxf = max(maxf, freq[s[r]])

            if (r - l) + 1 - maxf > k:
                freq[s[l]] -= 1
                res = max(res, (r - l))
                l += 1
            else:
                res = max(res, (r - l) + 1)
        return res






        

        