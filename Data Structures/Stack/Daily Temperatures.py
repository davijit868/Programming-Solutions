'''

Problem 739
https://leetcode.com/problems/daily-temperatures/

'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for i in range(len(temperatures))]
        
        # Naive Solution
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output[i] = j - i
                    break
        
        # Monotonic Stack
        stack = []
        for i in range(len(temperatures)):
            while len(stack):
                last = stack[-1]
                if temperatures[last] < temperatures[i]:
                    stack.pop()
                    output[last] = i - last
                else:
                    break
            stack.append(i)
        
        return output
        
