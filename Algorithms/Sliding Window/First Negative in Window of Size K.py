'''

First negative integer in every window of size k
https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1

'''

from collections import deque

def printFirstNegativeInteger(A, N, K):
    queue = deque()
    ans = []
    for i in range(K):
        if A[i] < 0:
            queue.append(i)
    if not queue:
        ans.append(0)
    else:
        ans.append(A[queue[0]])

    for i in range(K, N):
        while queue and queue[0] <= (i-K):
            queue.popleft()
        if A[i] < 0:
            queue.append(i)
        if not queue:
            ans.append(0)
        else:
            ans.append(A[queue[0]])
    return ans


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1

if __name__ == "__main__":
    main()

