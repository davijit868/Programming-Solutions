'''

Problem 417 | Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/

'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h = len(heights)
        w = len(heights[0])
        
        pacific = [[False for i in range(w)] for j in range(h)]
        atlantic = [[False for i in range(w)] for j in range(h)]
        
        def pacific_span(row, col, visited):
            visited[row][col] = True
            down = left = right = up = False
            if row <= 0 or col <= 0:
                return True
            if not visited[row-1][col] and heights[row-1][col] <= heights[row][col]:
                down = pacific_span(row-1, col, visited)
            if not visited[row][col-1] and heights[row][col-1] <= heights[row][col]:
                left = pacific_span(row, col-1, visited)
            if row + 1 < h and not visited[row+1][col] and heights[row+1][col] <= heights[row][col]:
                right = pacific_span(row+1, col, visited)
            if col + 1 < w and not visited[row][col+1] and heights[row][col+1] <= heights[row][col]:
                up = pacific_span(row, col+1, visited)
            
            if down or left or right or up:
                return True
            else:
                return False
            
        def atlantic_span(row, col, visited):
            visited[row][col] = True
            down = left = right = up = False
            if row == h-1 or col == w-1:
                return True
            if row - 1 >= 0 and not visited[row-1][col] and heights[row-1][col] <= heights[row][col]:
                down =  atlantic_span(row-1, col, visited)
            if col - 1 >= 0 and not visited[row][col-1] and heights[row][col-1] <= heights[row][col]:
                left = atlantic_span(row, col-1, visited)
            if not visited[row+1][col] and heights[row+1][col] <= heights[row][col]:
                right = atlantic_span(row+1, col, visited)
            if not visited[row][col+1] and heights[row][col+1] <= heights[row][col]:
                up =  atlantic_span(row, col+1, visited)
            
            if down or left or right or up:
                return True
            else:
                return False
            
        for row in range(h):
            for col in range(w):
                visited = [[False for i in range(w)] for j in range(h)]
                pacific[row][col] = pacific_span(row, col, visited)
                visited = [[False for i in range(w)] for j in range(h)]
                atlantic[row][col] = atlantic_span(row, col, visited)
                
        ans = []
        
        for row in range(h):
            for col in range(w):
                if pacific[row][col] and atlantic[row][col]:
                    ans.append([row, col])
            
        return ans
      
