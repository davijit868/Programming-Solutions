'''

Problem 290 | Word Pattern
https://leetcode.com/problems/word-pattern/

'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lookup = {}
        s = s.split()
        if len(pattern) != len(s) or len(set(pattern)) != len(set(s)): return False
        for i in range(len(pattern)):
            if pattern[i] not in lookup.keys():
                lookup[pattern[i]] = s[i]
            elif lookup[pattern[i]] != s[i]:
                return False
        return True
        
