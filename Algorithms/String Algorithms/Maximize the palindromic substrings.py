def Solve(SL,PL,S,P):
    P_dict = {}
    for i in P:
        if i not in P_dict:
            P_dict[i] = 1
        else:
            P_dict[i] += 1
    S_dict = {}
    for i in P_dict.keys():
        S_dict[i] = S.count(i)
    i = 1
    flag = False
    while True:
        for key,value in P_dict.items():
            if S_dict[key] < i * P_dict[key]:
                flag = True
                break
        if flag:
            return i-1
        else:
            i += 1
 
SL,PL = map(int,input().split())
 
S = input()
 
P = input()
 
out_ = Solve(SL,PL,S,P)
 
print (out_)
