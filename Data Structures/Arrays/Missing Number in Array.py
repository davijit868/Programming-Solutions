'''

Missing number in array
https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1

'''

class Solution:
    def MissingNumber(self,array,n):
        # code here
        total = sum(array)
        return int(((n*(n+1))/2) - total)

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
