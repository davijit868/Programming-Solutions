'''

https://www.hackerrank.com/challenges/linkedin-practice-dynamic-programming-lcs/problem

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())
#print(n,m)
N = list(map(int,input().split()))
M = list(map(int,input().split()))
arr = [[0 for _ in range(m+1)] for _ in range(n+1)] 
for i in range(1,n+1):
    for j in range(1,m+1):
        if N[i-1] == M[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i][j-1],arr[i-1][j])

i = n 
j = m  
lst = []
while i > 0 and j > 0:
    #print(arr[i][j])
    #print(i,j)
    if arr[i][j] == arr[i-1][j]:
        i = i - 1
    elif arr[i][j] == arr[i][j-1]:
        j = j - 1
    else:
        i = i - 1
        j = j - 1
        lst.insert(0,M[j])
for i in lst:
    print(i, end=" ")
