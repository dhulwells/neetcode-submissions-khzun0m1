class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check rows
        for i in range(9):
            rows = [board[i][j] for j in range(9) if board[i][j] != "."]
            if len(rows) != len(set(rows)):
                return False
        
        #check cols
        for j in range(9):
            cols = [board[i][j] for i in range(9) if board[i][j] != "."]
            if len(cols) != len(set(cols)):
                return False
        
        #check sub boxes
        boxes = [set() for _ in range(9)]

        for k in range(9):
            for l in range(9):
                val = board[k][l]
                if val != ".":
                    box_index = (k // 3) * + 3 + (l // 3)
                    if val in boxes[box_index]:
                        return False
                    boxes[box_index].add(val)

        #return True if we made it here
        return True

            