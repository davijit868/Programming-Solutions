n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# First solve whether it can be done or not
counted = []
count = 0
flag = False
for i in A + B:
    if i not in counted:
        counted.append(i)
        if (A.count(i) + B.count(i)) % 2 != 0:
            flag = True
            break
if flag:
    print(-1)
else:
    #print(1)
    for i in range(n):
        if A[i] != B[i]:
            num = B[i]
            for j in range(i+1,n):
                if A[j] != B[j]:
                    if A[j] == num:
                        A[j] = A[i]
                        A[i] = num
                        count += 1
                        break
                    elif B[j] == num:
                        B[j] = A[i]
                        A[i] = num
                        count += 1
                        break
                        
print(count)
