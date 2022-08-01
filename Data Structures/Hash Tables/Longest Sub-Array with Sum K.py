'''

Longest Sub-Array with Sum K.py
https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

'''

class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        
        look_up = {}
        total = 0
        ans = 0
        for i in range(N):
            total += A[i]
            if total == K:
                ans = i + 1
            elif (total - K) in look_up:
                ans = max(ans, i - look_up[total - K])
                
            if total not in look_up:
                look_up[total] = i
        return ans
        
for _ in range(0,int(input())):
    
    n, K = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, K))

