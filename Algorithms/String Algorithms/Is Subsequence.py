'''

https://leetcode.com/problems/is-subsequence/

'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for i in s:
            flag = False
            for j in range(start, len(t)):
                if i == t[j]:
                    flag = True
                    start = j + 1
                    break
            if not flag:
                return False
        return True
      
