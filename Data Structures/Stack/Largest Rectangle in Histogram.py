'''

Problem 84 | Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/

'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
        
