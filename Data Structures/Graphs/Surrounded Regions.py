'''

Problem 130 | Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        
        def dfs(r, c):
            if r >= 0 and r < row and c >= 0 and c < col:
                if board[r][c] == "O":
                    board[r][c] = "T"
                    dfs(r-1, c)
                    dfs(r+1, c) 
                    dfs(r, c-1)
                    dfs(r, c+1)
                    
            
        for i in range(col):
            if board[0][i] == "O":
                dfs(0, i)
        for i in range(1, row):
            if board[i][col-1] == "O":
                dfs(i, col-1)
        for i in range(col-1):
            if board[row-1][i] == "O":
                dfs(row-1, i)
        for i in range(1, row-1):
            if board[i][0] == "O":
                dfs(i, 0)
      
        for i in range(row):
            for j in range(col):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        
        
            
