'''

Problem 695 | Max Area of Island
https://leetcode.com/problems/max-area-of-island/

'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False for i in range(col)] for j in range(row)]
        max_area = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not visited[i][j]:
                    
                    def bfs(r, c):
                        if r >= 0 and r < row and c >= 0 and c < col:
                            if visited[r][c] or grid[r][c] == 0:
                                return 0
                            visited[r][c] = True
                            return 1 + bfs(r-1, c) + bfs(r+1, c) + bfs(r, c-1) + bfs(r, c+1) 
                        else:
                            return 0
                    
                    area = bfs(i, j)
                        
                    max_area = max(area, max_area)
        return max_area
