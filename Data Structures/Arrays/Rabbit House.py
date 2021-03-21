'''

https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14

'''

t = int(input())
for case in range(t):
    r, c = map(int, input().split())
    s = 0
    arr = []
    
    for i in range(r):
        row = list(map(int, input().split()))
        arr.append(row)
        
    for i in range(r):
        for j in range(c):
            # print("i:", i, "j:", j)
            if j < c-1: 
                h = abs(arr[i][j] - arr[i][j+1])
                if h > 1:
                    if arr[i][j] < arr[i][j+1]:
                        arr[i][j] += h-1
                    else:
                        arr[i][j+1] += h-1
                    s += h-1
            if i < r-1:
                v = abs(arr[i][j] - arr[i+1][j])
                if v > 1:
                    if arr[i][j] < arr[i+1][j]:
                        arr[i][j] += v-1
                    else:
                        arr[i+1][j] += v-1
                    s += v-1
                    
    print("Case #{0}: {1}".format(case+1, s))
