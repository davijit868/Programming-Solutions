'''

Problem 844 | Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/

'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:        
        def function(seq):
            skip = 0
            for i in reversed(seq):
                if i == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield i
        return all(x == y for x, y in itertools.zip_longest(function(s), function(t)))
      
