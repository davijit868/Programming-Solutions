'''

Problem Help Classmates
https://practice.geeksforgeeks.org/problems/fab3dbbdce746976ba35c7b9b24afde40eae5a04/1/#

'''

class Solution:
    def help_classmate(self, arr, n):
        stack = []
        ans = []
        for i in range(len(arr) - 1, -1, -1):
            flag = True
            while len(stack):
                if stack[-1] >= arr[i]:
                    stack.pop()
                else:
                    ans.append(stack[-1])
                    flag = False
                    break   
            if flag:
                ans.append(-1)
                    
            stack.append(arr[i])
        
        return ans[::-1]
        

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [ int(x) for x in input().split() ]
        obj = Solution()
        result = obj.help_classmate(arr,n)
        for i in result:
            print(i,end=' ')
        print()

