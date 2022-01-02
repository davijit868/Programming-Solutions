'''

https://www.geeksforgeeks.org/program-print-substrings-given-string/


'''

s = input()
answer = []

def recursion(seq, cur):
    if not len(seq):
        answer.append(cur)
    else:
        recursion(seq[1:], cur)
        recursion(seq[1:], cur + seq[0])

recursion(s, "")
print(answer)
 
