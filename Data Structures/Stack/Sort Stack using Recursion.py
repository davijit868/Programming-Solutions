'''

Sort Stack using Recursion
https://www.geeksforgeeks.org/sort-a-stack-using-recursion/

'''

class Solution:
    
    def insert_sort(self, s, num):
        if len(s) == 0 or s[-1] <= num:
            s.append(num)
        else:
            temp = s.pop()
            self.insert_sort(s, num)
            s.append(temp)
    
    def sorted(self, s):
        if s:
            temp = s.pop()
            self.sorted(s)
            self.insert_sort(s, temp)
            
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends
