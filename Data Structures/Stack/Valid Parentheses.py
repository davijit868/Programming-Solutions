'''

Problem 20 | Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif len(stack):
                if stack[-1] == "(" and i == ")":
                    stack.pop(-1)
                elif stack[-1] == "{" and i == "}":
                    stack.pop(-1)
                elif stack[-1] == "[" and i == "]":
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
        if len(stack):
            return False
        else:
            return True
        
            
