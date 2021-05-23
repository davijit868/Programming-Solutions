'''

https://leetcode.com/problems/longest-common-subsequence/submissions/

'''
class Solution:
    look_up = [[-1 for i in range(1001)] for j in range(1001)] 
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        Solution.look_up = [[-1 for i in range(1001)] for j in range(1001)]
        return self.longestCommonSubsequenceRecursion(text1, text2, len(text1), len(text2))
      
    def longestCommonSubsequenceRecursion(self, text1, text2, m, n):
        if m == 0 or n == 0:
            return 0
        if Solution.look_up[m][n] != -1:
            return Solution.look_up[m][n]
        if text1[m-1] == text2[n-1]:
            Solution.look_up[m][n] = 1 + self.longestCommonSubsequenceRecursion(text1, text2, m-1, n-1)
        else:
            Solution.look_up[m][n] = max(self.longestCommonSubsequenceRecursion(text1, text2, m, n-1),
                                         self.longestCommonSubsequenceRecursion(text1, text2, m-1, n))
        return Solution.look_up[m][n]
        
