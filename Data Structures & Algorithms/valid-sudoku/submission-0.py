from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # hashamp 
        # one for each box
        # one for each row
        # one for each col 
        hash_box = defaultdict(set)
        hash_row = defaultdict(set)
        hash_col = defaultdict(set)
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != ".":
                    box = (row // 3) * 3 + (col // 3)
                    if num in hash_box[box] or num in hash_row[row] or num in hash_col[col]:
                        return False
                    else:
                        hash_box[box].add(num)
                        hash_row[row].add(num)
                        hash_col[col].add(num)
        return True
                

        