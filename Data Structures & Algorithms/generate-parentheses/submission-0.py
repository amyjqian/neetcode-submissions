class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, openn, close):
            if len(s) == 2 * n:
                ans.append(s)
                return 
            
            if openn < n:
                backtrack(s + "(", openn + 1, close)
            
            if close < openn:
                backtrack(s + ")", openn, close + 1)
        
        backtrack("", 0, 0)
        return ans
            

        