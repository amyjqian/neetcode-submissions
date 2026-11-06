class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start at 0, 0
        # for each character append {char: index}
        # if char in dict: calculate length
        # move l = {char: index}
        if s == "":
            return 0
        l, r = 0, 0
        seen = set()
        best = 1
        while r < len(s):
            if s[r] not in seen:
                curr = (r - l) + 1
                best = max(best, curr)
                seen.add(s[r])
                r += 1
            else:
                while l < r and s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
                r += 1
                
            # print(f"l: {l}, s[l]; {s[l]}")
            # print(f"r: {r}, s[r]; {s[r]}")
        return best
        