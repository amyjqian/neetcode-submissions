class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        best = 0
        ans = ""
        for i in range(len(s)):
            l = r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > best:
                    best = r - l + 1
                    ans = s[l: r + 1]
                l -= 1
                r += 1 
            
            l, r = i, i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > best:
                    best = r - l + 1
                    ans = s[l: r + 1]
                    # print(f"inside loop ans: {s[l:r + 1]}")
                l -= 1
                r += 1 
            # print(f"i: {i}")
            # print(f"best: {best}")
            # print(f"ans: {ans}")
        return ans

            


        