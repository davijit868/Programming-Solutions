# A = list(map(int, input().split()))
A = [1, 2, 3, 4, 5]
for i in range(len(A)):
    for j in range(i, len(A)):
        for k in range(i, j+1):
            print(A[k], end=' ')
        print('\n')
