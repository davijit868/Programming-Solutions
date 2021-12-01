'''

Problem 85 | Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/

'''

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not len(matrix):
            return 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = int(matrix[row][col])
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] != 0:
                    matrix[row][col] = int(matrix[row][col]) + int(matrix[row-1][col])
                else:
                    matrix[row][col] = 0
        max_by_row = []
        for i in range(len(matrix)):
            max_by_row.append(self.largest_rectangle_in_histogram(matrix[i]))
        
        return max(max_by_row)
        
        
    def largest_rectangle_in_histogram(self, heights):
        left_stack = []
        left = []
        for i in range(len(heights)):
            left_idx = i
            left_flag = False
            while len(left_stack):
                if heights[left_stack[-1]] >= heights[i]:
                    left_idx = left_stack.pop(-1)
                else:
                    left_flag = True
                    left_idx = left_stack[-1]
                    break
            if left_flag:
                left.append(left_idx + 1)
            else:
                left.append(0)
            left_stack.append(i)
            
        right_stack = []
        right = [i for i in range(len(heights))]
        for i in range(len(heights)-1, -1, -1):
            right_idx = i
            right_flag = False
            while len(right_stack):
                if heights[right_stack[-1]] >= heights[i]:
                    right_idx = right_stack.pop(-1)
                else:
                    right_flag = True
                    right_idx = right_stack[-1]
                    break
            if right_flag:
                right[i] = right_idx - 1
            else:
                right[i] = len(heights) - 1
            right_stack.append(i)
        
        max_len_by_idx = []
        for i in range(len(heights)):
            max_len_by_idx.append((right[i] - left[i] + 1)*heights[i])
        
        return max(max_len_by_idx)
      
