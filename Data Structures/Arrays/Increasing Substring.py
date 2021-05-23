'''

https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882

'''

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

T = int(input())
for t in range(T):
    l = int(input())
    arr = input()
    op = []
    for i in range(l):
        d = 1
        m = letters.index(arr[i])
        for j in range(i-1, -1, -1):
            if letters.index(arr[j]) < m:
                m = letters.index(arr[j])
                d += 1
            else:
                break
        op.append(d)
    output = "Case #{0}:".format(t+1)
    for i in op:
        output += " " + str(i)
    print(output)
