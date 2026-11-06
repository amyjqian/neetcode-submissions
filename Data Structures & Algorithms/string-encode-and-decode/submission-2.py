class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            index = i
            while s[index] != "#":
                index += 1
            length = int(s[i:index])
            i = index + 1
            word = s[i:i+length]
            res.append(word)
            i += length
        return res
        
