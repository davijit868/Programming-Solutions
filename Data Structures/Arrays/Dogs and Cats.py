'''
Google Kickstart Round G 2021

https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3771
https://leetcode.com/playground/VSa2rWCF

'''

T = int(input())
for t in range(T):
    N, D, C, M = map(int, input().split())
    S = input()
    result = "YES"
    for i in range(N):
        if D > 0:
            if S[i] == 'C' and C > 0:
                C -= 1
            elif S[i] == 'C' and C == 0:
                if 'D' not in S[i:]:
                    result = "YES"
                else:
                    result = "NO"
                    break
            elif S[i] == 'D':
                D -= 1
                C += M
        elif D == 0 and 'D' in S[i:]:
            result = "NO"
            break
        elif D == 0 and 'D' not in S[i:]:
            result = "YES"
            break
    print("Case #{}: {}".format(t+1, result))
