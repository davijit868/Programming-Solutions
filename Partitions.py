g = []
c = 0
def partition(a, t):
    global c
    for i in range(1,len(a)+1):
        t2 = t[:]
        temp = a[:i]
        s = 0
        for j in temp:
            s += j
        if s >=l and s <= r:
            t.append(temp)
            if len(a[i:]) == 0:
                c += 1
                #print(t)
            partition(a[i:],t)
            t = t2

n, l, r = map(int,input().split())
a = list(map(int,input().split()))
partition(a,[])
# for i in g:
#     print(i)
print(c % 1000000007)
