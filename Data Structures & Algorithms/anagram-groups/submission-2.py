class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # build frequency list for each str
        # check if it's in freq 
        # if yes append 
        seen = {}
        for s in strs:
            freq = [0] * 26
            for i in range(len(s)):
                freq[ord(s[i]) - ord('a')] += 1
            
            tup = tuple(freq)

            if tup in seen:
                seen[tup].append(s)
            else:
                seen[tup] = [s]
        
        return [value for key, value in seen.items()]


        