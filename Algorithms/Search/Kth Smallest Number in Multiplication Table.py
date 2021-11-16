'''

Problem 668
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

'''

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m > n:
            m, n = n, m
 
        def search(number):
            ans = 0
            for i in range(1, min(m, number) + 1):
                ans += min(n, number // i)
            return ans
        
        left = 1
        right = m * n
        while(left < right):
            mid = (left + right) // 2
            if search(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left
        
