'''

https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/

'''

class Solution:
    def bfsOfGraph(self, V, adj):
        queue = []
        visited = [0 for i in range(V)]
        queue.append(0)
        visited[0] = 1
        bfs_traversal = []
        bfs_traversal.append(0)
        while(len(queue)):
            node = queue.pop(0)
            for i in adj[node]:
                if visited[i] == 0:
                    bfs_traversal.append(i)
                    visited[i] = 1
                    queue.append(i)
        return bfs_traversal


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
        
