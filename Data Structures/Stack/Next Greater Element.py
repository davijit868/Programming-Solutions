'''

Next Greater Element 
https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1/#

'''

class Solution:
    def nextLargerElement(self,arr,n):
        stack = []
        ans = []
        
        for i in range(n - 1, -1, -1):
            while len(stack):
                if arr[i] < stack[-1]:
                    ans.append(stack[-1])
                    break
                else:
                    stack.pop(-1)
                
            else:
                ans.append(-1)
            stack.append(arr[i])
                
        return ans[::-1]

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()

