'''

Write a program to create all partitions of a string

'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        
        def backtrack(cur, l):
            if not cur:
                answer.append(l[:])
            for i in range(1, len(cur) + 1):
                l.append(cur[:i])
                backtrack(cur[i:], l[:])
                l.pop(-1)
            
        backtrack(s, [])
        return answer
      
