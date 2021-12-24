'''

https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1#

'''

class Solution:
    def dfsOfGraph(self, V, adj):
        visited = [0 for i in range(V)]
        output = []
        
        def recursion(curr):
            if visited[curr] != 1:
                output.append(curr)
                visited[curr] = 1
                # stack.append(i)
                for i in adj[curr]:
                    recursion(i)
                
        recursion(0)   
        return output

if __name__ == '__main__':
    T= int(input())
    while T > 0:
        V, E = map(int, input().split())
        adj = [[] for i in range(V + 1)]
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
