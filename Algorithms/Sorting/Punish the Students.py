'''

Punish the Students
https://practice.geeksforgeeks.org/problems/punish-the-students5726/1

'''

class Solution:
    def shouldPunish (self, roll, marks, n, avg):
        count = 0
        for i in range(n):
            for j in range(n - i - 2):
                if roll[j] > roll[j + 1]:
                    temp = roll[j]
                    roll[j] = roll[j+1]
                    roll[j+1] = temp
                    count +=2
        
        if ((sum(marks) - count)/n) > avg:
            return 1
        else:
            return 0


t = int (input ())
for tc in range (t):
    n, avg = input ().split ()
    n = int (n)
    avg = float (avg)
    roll = list(map(int, input().split()))
    marks = list(map(int, input().split()))
    ob=Solution()
    print (ob.shouldPunish (roll, marks, n, avg))
