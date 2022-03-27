'''

Problem 417 | Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/

'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height, width = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited, prev_height):
            if (r, c) in visited or r < 0 or c < 0 or r == height or c == width or heights[r][c] < prev_height:
                return 
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            
        for c in range(width):
            dfs(0, c, pacific, heights[0][c])
            dfs(height - 1, c, atlantic, heights[height - 1][c])
            
        for r in range(height):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, width - 1, atlantic, heights[r][width - 1])
        
        ans = []
        
        for r in range(height):
            for c in range(width):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append((r, c))
        return ans
