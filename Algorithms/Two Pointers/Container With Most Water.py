'''

Problem 11 | Container With Most Water
https://leetcode.com/problems/container-with-most-water/

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        ans = 0
        while start < end:
            area = (end - start) * min(height[start], height[end])
            if area > ans:
                ans = area
            if height[start] < height[end]:
                start +=1
            else:
                end -= 1
        return ans
