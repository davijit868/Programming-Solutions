'''

Leetcode 84 | Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/

'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rectangle_area = []
        for idx in range(len(heights)):
            height = heights[idx]
            left = idx
            right = idx
            while left >= 0:
                if heights[left] < height:
                    break
                left -= 1
            while right <= len(heights)-1:
                if heights[right] < height:
                    break
                right += 1
            width = (right - left - 1)
            area = width*height
            rectangle_area.append(area)
        return max(rectangle_area)
        
