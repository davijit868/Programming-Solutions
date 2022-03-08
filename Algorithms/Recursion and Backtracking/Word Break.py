'''

Problem 139 | Word Break
https://leetcode.com/problems/word-break/

'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def recursion(start):
            if start >= len(s):
                return True
            flag = True
            for word in wordDict:
                l = len(word)
                if start + l <= len(s) and s[start: start + l] == word:
                    flag = False
                    if recursion(start + l): return True
            if flag:
                return False
        
        return recursion(0)
                    
