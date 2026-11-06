from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        ans = []
        count = 0
        for s in strs:
            word = "".join(sorted(s))
            if word in d:
                index = d[word]
                ans[index].append(s)
            else:
                d[word] = count
                count += 1
                ans.append([s])
        return ans
            