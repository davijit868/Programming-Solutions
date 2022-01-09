'''

Problem 131 | Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/

'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        
        def palindrome(s):
            if s == s[::-1]: return True
            else: return False
        
        def backtrack(cur, l):
            if not cur:
                answer.append(l[:])
            for i in range(1, len(cur) + 1):
                if palindrome(cur[:i]):
                    l.append(cur[:i])
                    backtrack(cur[i:], l[:])
                    l.pop(-1)
            
        backtrack(s, [])
        return answer
      
