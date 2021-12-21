'''

Problem 200 | Number of Islands
https://leetcode.com/problems/number-of-islands/

'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[0 for i in range(cols)] for j in range(rows)]
        islands = 0
        
        def breadth_first_search(row, col):
            if row >= 0  and row < rows and col >= 0 and col < cols:
                if grid[row][col] == "1" and visited[row][col] == 0:
                    visited[row][col] = 1
                    breadth_first_search(row + 1, col)
                    breadth_first_search(row, col + 1)
                    breadth_first_search(row - 1, col)
                    breadth_first_search(row, col - 1)
            return 
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and visited[row][col] == 0:
                    breadth_first_search(row, col)
                    islands += 1
        return islands
                    
