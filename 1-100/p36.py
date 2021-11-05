'''
Problem constraints: input board is 9x9 with all values being 1-9 or '.'.
Therefore do not need to check that values of board are from a valid set {1,2,3,4,5,6,7,8,.}

Could make it faster by iterating only the columns we need. I.e. all rows, all columns and only 0,3,6 for the subsquares.
'''
class Solution:
    def checkGroup(self, num_arr):
        return len(num_arr) == len(set(num_arr))

    def isValidSudoku(self, board):
        sz = len(board)
        sub_sz = 3
        for row in range(sz):
            for col in range(sz):
                # if it's top of column check that column
                if row == 0:
                    col_vals = [board[r][col] for r in range(sz) if board[r][col] != '.']
                    if not self.checkGroup(col_vals): return False
                # if it's start of a row check that row
                if col == 0:
                    row_vals = [board[row][c] for c in range(sz) if board[row][c] != '.']
                    if not self.checkGroup(row_vals): return False
                # if it's top-left of a sub-square check it
                if row % sub_sz == 0 and col % sub_sz == 0:
                    sub_vals = [board[n][m] for n in range(row, row+sub_sz) for m in range(col, col+sub_sz) if board[n][m] != '.']
                    if not self.checkGroup(sub_vals): return False
        return True




if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    sol = Solution()
    print(sol.isValidSudoku(board))