'''

https://leetcode.com/problems/find-the-town-judge/

'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            graph[i][i] = 1
        for i in trust:
            graph[i[0]-1][i[1]-1] = 1
        index = -1
        for i in range(n):
            if graph[i].count(1) == 1:
                flag = True
                for j in range(n):
                    if graph[j][i] != 1:
                        flag = False
                        break
                if flag:
                    index = i+1
        return index
        
            
        
