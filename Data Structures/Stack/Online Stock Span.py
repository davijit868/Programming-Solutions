'''

Problem 901 | Online Stock Span
https://leetcode.com/problems/online-stock-span/

'''

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        curr = 1
        while len(self.stack) and self.stack[-1][0] <= price:
            curr += self.stack.pop()[1]
        self.stack.append([price, curr])
        return curr

obj = StockSpanner()
param_1 = obj.next(price)
