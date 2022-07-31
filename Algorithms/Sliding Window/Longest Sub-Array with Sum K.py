'''


https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

'''

class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        #Complete the function
        start = end = 0
        ans = 0
        total = 0
        while end <N:
            #print(start, end)
            if total < K:
                #total += A[end]
                end += 1
            elif total == K:
                ans = max(ans, end-start + 1)
                end += 1
            elif total > K:
                while total >K:
                    total -= A[start]
                    start += 1
                if total == K:
                    ans = max(ans, end - start + 1)
                end +=1
        
        return ans
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, K = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, K))




# } Driver Code Ends
