'''

Problem 42 | Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]]
        for i in range(1, len(height)):
            left.append(max(left[-1], height[i-1]))
        
        right = [0 for i in range(len(height))]
        right[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(right[i+1], height[i+1])
        
        water = []
        for i in range(len(height)):
            val = min(left[i], right[i])
            if val - height[i] > 0:
                water.append(val-height[i])
            else:
                water.append(0)
        total = sum(water)
        return total
        
