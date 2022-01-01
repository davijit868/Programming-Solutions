'''

Problem 5 | Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[0 for i in range(l)] for j in range(l)]
        
        for i in range(l):
            dp[i][i] = True
            output = s[i]
        
        for start in range(l - 1, -1, -1):
            for end in range(start + 1, l):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1] == True:
                        dp[start][end] = True
                        if end - start + 1 > max_len:
                            max_len = end - start + 1
                            output = s[start:end + 1]
        return output
                    
