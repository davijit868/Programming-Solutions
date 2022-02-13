'''

Problem 844 | Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/

'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack, t_stack = [], []
        
        for i in s:
            if i == '#':
                if len(s_stack):
                    s_stack.pop(-1)
            else:
                s_stack.append(i)
        s = "".join(s_stack)
        
        for i in t:
            if i == '#':
                if len(t_stack):
                    t_stack.pop(-1) 
            else:
                t_stack.append(i)
        t = "".join(t_stack)
        
        if s == t:
            return True
        else:
            return False
            
