'''

Max Sum Subarray of size K
https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

'''

class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        total = 0
        for i in range(K):
            total += Arr[i]
        ans = total
        i = K
        while i < len(Arr):
            total += Arr[i]
            total -= Arr[i-K]
            if total > ans:
                ans = total
            i += 1
        return ans
            

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
