'''

Finding the optimal path between the first and last element of an array where each element is from 1 to N
Every element is associated with a cost that needs to be paid to go through that element
It is possible to jump to another element based on a criterian

'''

def optimal(node,cost):
    if node == n-1:
        global_cost.append(cost)
    else:
        for i in range(n):
            if path[node][i] == 1:
                optimal(i,cost+A[i])

global_cost = []
T = int(input())
for _ in range(T):
    n, k = map(int,input().split())
    A = list(map(int,input().split()))
    path = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        path[i][i+1] = 1
        temp = (i+1)+((i+1)%k)+1
        if temp <= n:
            path[i][temp-1] = 1
    node = 0
    cost = A[0]
    optimal(0,cost)
    print(min(global_cost))
    
                
