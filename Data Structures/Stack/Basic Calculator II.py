'''

Problem 227 | Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/

'''

class Solution:
    def calculate(self, s: str) -> int:
        operators = ['/', '*', '+', '-']
        exp = []
        cur = ""
        for i in s:
            if i.isnumeric():
                cur += i
            elif i in operators:
                if len(cur):
                    exp.append(cur)
                    cur = ""
                exp.append(i)
            elif i == ' ':
                if len(cur):
                    exp.append(cur)
                    cur = ""
        exp.append(cur)
        
        sign = []
        stack = []
        prev_sign = ""
        for i in exp:
            if i.isnumeric():
                if prev_sign in ['*', '/']:
                    top = int(stack.pop(-1))
                    if prev_sign == '*':
                        stack.append(top*int(i))
                    elif prev_sign == '/':
                        stack.append(top//int(i))
                else:
                    stack.append(i)
            else:
                if i in ['+', '-']:
                    sign.append(i)
                prev_sign = i
        
        left = int(stack[0])
        if sign:
            for i in range(1, len(stack)):
                if sign[i-1] == '+':
                    left = left + int(stack[i])
                elif sign[i-1] == '-':
                    left = left - int(stack[i])
        return left
                    
