from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for i in range(len(s)):
                freq[ord(s[i]) - ord("a")] += 1 
            tup = tuple(freq)
            seen[tup].append(s)
        
        return [value for key, value in seen.items()]




        


        