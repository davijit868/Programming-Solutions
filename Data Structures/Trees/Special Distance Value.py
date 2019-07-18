import math
 
# This can be replaced using math.log and then math.ceil
# I couldn't do it because of time constraint
def cur(n):
    
    
    i = 1
    while True:
        if n < pow(2,i) and n >= pow(2,i-1):
            return i
        i += 1
        
def Solve(N):
    level = cur(N)
    s = 0
    for i in range(1,pow(2,level)):
        current_level = cur(i)
        for j in range(current_level+1,level+1):
            s += (j - current_level)*pow(2,(j - current_level))
    return s % 1000000007
 
T = int(input())
 
for _ in range(T):
 
    N = int(input())
 
    out_ = Solve(N)
 
    print(out_)
