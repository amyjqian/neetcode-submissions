class Solution:

    def encode(self, strs: List[str]) -> str:
        # start with pound 
        # length 
        # string 
        ans = ""
        for s in strs:
            length = len(s)
            ans += str(length)
            ans += "#"
            ans += s
        # print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            length = ""
            while i < len(s) and s[i] != "#":
                length += s[i]
                i += 1
            # print(length)
            length = int(length)
            i += 1
            ans.append(s[i: i + length])
            i += length
        return ans

