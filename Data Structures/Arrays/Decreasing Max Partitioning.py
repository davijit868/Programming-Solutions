'''

https://www.hackerearth.com/challenges/competitive/june-circuits-17/algorithm/decreasing-max-partitioning/

Partially Solved

'''

c = 0
def partition(a, t):
    global c, sg
    for i in range(1,len(a)+1):
        t2 = t[:]
        temp = a[:i]
        
        if len(t) == 0:
            t.append(temp)
            if len(a[i:]) == 0:
                c += 1
                #print(t)
            partition(a[i:],t)
            t = t2
        
        elif max(t[-1]) >= max(temp):
            t.append(temp)
            if len(a[i:]) == 0:
                c += 1
                #print(t)
            partition(a[i:],t)
            t = t2
       
        

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    partition(a,[])
# for i in g:
#     print(i)
    print(c % 1000000007)
    c = 0
