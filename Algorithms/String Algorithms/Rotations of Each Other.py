'''

Problem: Check if strings are rotations of each other or not
https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1

'''

class Solution:
    def areRotations(self,s1,s2):
        if len(s1) == len(s2):
            temp = s1 + s1
            if s2 in temp:
                return 1
            else:
                return 0
        else:
            return 0
        
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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s1=str(input())
        s2=str(input())
        if(Solution().areRotations(s1,s2)):
            print(1)
        else:
            print(0)
    
