'''

Longest Sub-Array with Sum K
https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

'''

class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        ans = 0
        for start in range(N):
            total = 0
            for end in range(start, N):
                total += A[end]
                if total == K:
                    ans = max(ans, end-start+1)
        return ans

for _ in range(0,int(input())):
    
    n, K = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, K))

    
