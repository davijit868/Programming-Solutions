'''

Longest Common Substring
https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1#

'''

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        mx = 0
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if S1[i - 1] == S2[j - 1]:
                    dp[i][j] =  dp[i - 1][j - 1] + 1
                    if dp[i][j] > mx:
                        mx = dp[i][j]           
        return mx
 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = input().strip().split(" ")
        n, m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        ob = Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
