'''

Problem 139 | Word Break
https://leetcode.com/problems/word-break/

'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None]*len(s)
        def recursion(start):
            if start >= len(s):
                return True
            elif dp[start] == None:
                flag = False
                for word in wordDict:
                    l = len(word)
                    if start + l <= len(s) and s[start: start + l] == word:
                        if recursion(start + l): 
                            flag = True
                            dp[start] = True
                            return True
                dp[start] = False
                return False
            else:
                return dp[start]
        recursion(0)
        return dp[0]
        
                    
