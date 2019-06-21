def optimal(node,cost):
    print(node,cost)
    if node == n-1:
        globalcost.append(cost)
    else:
        for i in range(n):
            if path[node][i] == 1:
                optimal(i,cost+A[i])

globalcost = []
T = int(input())
for _ in range(T):
    n, k = map(int,input().split())
    A = list(map(int,input().split()))
    path = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        path[i][i+1] = 1
        temp = (i+1)+((i+1)%k)+1
        print(temp)
        if temp <= n:
            path[i][temp-1] = 1
    print(path)
    node = 0
    cost = A[0]
    optimal(0,cost)
    print(globalcost)
    print(min(globalcost))
    
                
