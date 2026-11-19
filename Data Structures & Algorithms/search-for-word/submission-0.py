class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(r, c, length):
            if length == len(word):
                return True 
            
            if not (0 <= r < len(board) and 0 <= c < len(board[0])) or board[r][c] != word[length]:
                return False 
            
            tmp = board[r][c]
            board[r][c] = "#"
            found = (backtrack(r + 1, c, length + 1) or
                     backtrack(r - 1, c, length + 1) or
                     backtrack(r, c + 1, length + 1) or
                     backtrack(r, c - 1, length + 1))
            board[r][c] = tmp
            return found
            
        
        return any(backtrack(r, c, 0) for r in range(len(board)) for c in range(len(board[0])))

        

        