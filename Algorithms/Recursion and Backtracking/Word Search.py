'''

Problem 79 | Word Search
https://leetcode.com/problems/word-search/

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = []
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    start.append([i, j])
        
        for i in start:
            visited = [[False for i in range(col)] for j in range(row)]
            visited[i[0]][i[1]] = True
            def traverse(x, y, word_idx):
                if x >= 0 and x < row and y >= 0 and y < col:
                    if visited[x][y] == False:
                        visited[x][y] = True
                        if board[x][y] == word[word_idx]:
                            # word_idx = word_idx + 1
                            if word_idx + 1 < len(word):
                                if traverse(x, y + 1, word_idx + 1) or traverse(x + 1, y, word_idx + 1) or \
                                       traverse(x, y - 1, word_idx + 1) or traverse(x - 1, y, word_idx + 1):
                                    return True
                                else:
                                    visited[x][y] = False        
                                    return False
                            else:
                                return True
                        else:
                            visited[x][y] = False
                            return False
                else:
                    return False
                    
            word_idx = 1
            if word_idx < len(word):
                x, y = i[0], i[1]
                if traverse(x, y + 1, word_idx) or traverse(x + 1, y, word_idx) or \
                   traverse(x, y - 1, word_idx) or traverse(x - 1, y, word_idx):
                    return True
            else:
                return True
        return False
        
