'''

Problem 310 | Minimum Height Trees
https://leetcode.com/problems/minimum-height-trees/

'''

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in edges:
            if i[0] not in adj:
                adj[i[0]] = [i[1]]
            else:
                adj[i[0]].append(i[1])
                
            if i[1] not in adj:
                adj[i[1]] = [i[0]]
            else:
                adj[i[1]].append(i[0])
        
        def height(node, visited):
            if node in visited or node not in adj.keys():
                return 0
            ht = max((height(i, visited + [node]) + 1) for i in adj[node])
            return ht
        
        ans = []
        
        for i in range(n):
            ans.append(height(i, []))
            
        m = min(ans)
        
        res = []
        for i in range(n):
            if ans[i] == m:
                res.append(i)
        
        return res
        
