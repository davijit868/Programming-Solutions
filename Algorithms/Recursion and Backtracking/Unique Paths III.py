'''

Problem 980
https://leetcode.com/problems/unique-paths-iii/

'''

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        zero_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zero_count += 1
                elif grid[i][j] == 1:
                    sx = i
                    sy = j
        
        def backtrack(x, y, zero_count):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == -1:
                return 0
            elif grid[x][y] == 2:
                if zero_count == -1:
                    return 1
                else:
                    return 0
            grid[x][y] = -1
            zero_count -= 1
            total_path = backtrack(x, y+1, zero_count) + \
                         backtrack(x+1, y, zero_count) + \
                         backtrack(x, y-1, zero_count) + \
                         backtrack(x-1, y, zero_count)
            grid[x][y] = 0
            zero_count += 1
            return total_path
            
        return backtrack(sx, sy, zero_count)
                
