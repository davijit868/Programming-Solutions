'''

Problem 784 | Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/

'''

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(word, start):
            if start == len(s):
                ans.append(word)
            
            for i in range(start, len(word)):
                if not word[i].isnumeric():
                    backtrack(word[:i] + word[i].lower() + word[i+1:], i+1)
                    backtrack(word[:i] + word[i].upper() + word[i+1:], i+1)
                elif i == len(s) - 1:
                    ans.append(word)
        backtrack(s, 0)
        return set(ans)
            
