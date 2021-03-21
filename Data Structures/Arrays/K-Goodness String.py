'''

https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3

'''

t = int(input())

for case in range(t):
    l, k = map(int, input().split())
    s = input()
    
    m = 0
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            m += 1
    
    if k>=m:
        print("Case #{0}: {1}".format(case+1, k-m))
    else:
        print("Case #{0}: {1}".format(case+1, m-k))
