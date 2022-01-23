'''

Problem 48 | Rotate Image
https://leetcode.com/problems/rotate-image/

'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        left, right = 0, len(matrix) - 1
        top, bottom = 0, len(matrix) - 1
        while left < right and top < bottom:
            for i in range(right-left):
                temp = matrix[top + i][left]
                matrix[top + i][left] = matrix[bottom][left + i]
                matrix[bottom][left + i] = matrix[bottom - i][right]
                matrix[bottom - i][right] = matrix[top][right - i]
                matrix[top][right - i] = temp
            left += 1
            right -=1
            top += 1
            bottom -= 1
        
