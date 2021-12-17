'''

Problem 221 | Maximal Square
https://leetcode.com/problems/maximal-square/

'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                
        def histogram():
            for i in range(1, len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 1:
                        matrix[i][j] += matrix[i-1][j]
        
        def max_square_per_row():
            max_area = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    height = matrix[i][j]
                    left, right = j, j
                    for k in range(j+1, len(matrix[0])):
                        if matrix[i][k] < height:
                            break
                        else:
                            right = k
                    for k in range(j-1, -1, -1):
                        if matrix[i][k] < height:
                            break
                        else:
                            left = k
                    width = (right - left + 1)
                    if width >= height:
                        area = height * height
                        if area > max_area:
                            max_area = area
            return max_area
                        
        histogram()
        return max_square_per_row()
        
