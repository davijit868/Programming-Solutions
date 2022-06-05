'''

Problem 51 | N-Queens
https://leetcode.com/problems/n-queens/

'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        pos_diag = set()
        neg_diag = set()
        def backtrack(arr, row):
            if len(arr) == n:
                ans.append(arr)
                return 
            for col in range(n):
                if col in arr or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                backtrack(arr + [col], row + 1)  
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
            
        backtrack([], -1)
        
        res = []
        for sol in ans:
            board = [["."] * n for i in range(n)]
            for i in sol:
                board[sol.index(i)][i] = 'Q'
            board = ["".join(row) for row in board]
            res.append(board)
        return res
        
