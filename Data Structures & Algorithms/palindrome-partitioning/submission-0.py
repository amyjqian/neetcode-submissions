class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def backtrack(i):
            if i == len(s):
                ans.append(path.copy())

            for j in range(i, len(s)):
                piece = s[i: j + 1]
                if piece == piece[::-1]:
                    path.append(piece)
                    backtrack(j + 1)
                    path.pop()
        
        backtrack(0)
        return ans

        