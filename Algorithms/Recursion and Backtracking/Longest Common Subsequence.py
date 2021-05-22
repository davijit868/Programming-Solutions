'''

https://leetcode.com/problems/longest-common-subsequence/

'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequenceRecursion(text1, text2, len(text1), len(text2))
        
    def longestCommonSubsequenceRecursion(self, text1, text2, m, n):
        if m == 0 or n == 0:
            return 0
        if text1[m-1] == text2[n-1]:
            return 1 + self.longestCommonSubsequenceRecursion(text1, text2, m-1, n-1)
        else:
            return max(self.longestCommonSubsequenceRecursion(text1, text2, m, n-1),
                       self.longestCommonSubsequenceRecursion(text1, text2, m-1, n))
