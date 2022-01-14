'''

Problem 73 | Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/

'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        zero_row, zero_col = [], []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zero_row.append(i)
                    zero_col.append(j)
        for i in range(row):
            for j in range(col):
                if (i in zero_row) or (j in zero_col):
                    matrix[i][j] = 0
                    
