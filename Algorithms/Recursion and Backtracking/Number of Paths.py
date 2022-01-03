'''

https://practice.geeksforgeeks.org/problems/number-of-paths0926/1/

'''

class Solution:
    def numberOfPaths (self, n, m):
        num_of_path = 0
        def recursion(i, j):
            print(i, j)
            nonlocal num_of_path
            if i == n - 1 and j == m - 1:
                num_of_path += 1
                return 
            elif i >= n or j >= m:
                return
            else: 
                recursion(i + 1, j)
                recursion(i, j + 1)
                
        recursion(0, 0)
        return num_of_path
    

if __name__ == '__main__': 
    ob = Solution()
    t = int(input())
    for _ in range (t):
        m, n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)
 
