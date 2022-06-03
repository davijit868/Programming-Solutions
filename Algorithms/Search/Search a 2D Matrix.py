'''

Problem 74 | Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        l_row, r_row = 0, len(matrix)
        while l_row <= r_row:
            m_row = (l_row + r_row) // 2
            if target  < matrix[m_row][-1]:
                r_row = m_row - 1
            elif target > matrix[m_row][-1]:
                l_row = m_row + 1
            else:
                return True
        
        l_col, r_col = 0, len(matrix[0]) - 1
        while l_col <= r_col:
            m_col = (l_col + r_col) // 2
            if target  < matrix[l_row][m_col]:
                r_col = m_col - 1
            elif target > matrix[l_row][m_col]:
                l_col = m_col + 1
            else:
                return True
              
        return False
            
        
