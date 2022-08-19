'''

Problem 150 | Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/

'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(i)
            else:
                right = stack.pop(-1)
                left = stack.pop(-1)
                if i == '+':
                    stack.append(int(left) + int(right))
                elif i == '-':
                    stack.append(int(left) - int(right))
                elif i == '*':
                    stack.append(int(left) * int(right))
                elif i == '/':
                    stack.append(int(left) / int(right))
      
        return int(stack[0])
