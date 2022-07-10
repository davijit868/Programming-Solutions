'''

Maximum Rectangular Area in a Histogram
https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1#

'''

class Solution:
    def getMaxArea(self,histogram):
        stack, right = [], []
        for i in range(len(histogram) - 1, -1, -1):
            flag = True
            while len(stack):
                if stack[-1][0] >= histogram[i]:
                    stack.pop()
                else:
                    right.append(stack[-1][1]-1)
                    flag = False
                    break
            if flag:
                right.append(len(histogram) - 1)
            stack.append((histogram[i], i))
        right = right[::-1]
        
        left, stack = [], []
        for i in range(len(histogram)):
            flag = True
            while len(stack):
                if stack[-1][0] >= histogram[i]:
                    stack.pop()
                else:
                    left.append(stack[-1][1] + 1)
                    flag = False
                    break
            if flag:
                left.append(0)
            stack.append((histogram[i],i))

        ans = []
        for i in range(len(histogram)):
            ans.append((right[i] - left[i] + 1)*histogram[i])
        
        return max(ans)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))

  
