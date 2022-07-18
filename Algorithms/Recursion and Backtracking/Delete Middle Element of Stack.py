'''

Delete Middle Element of Stack
https://practice.geeksforgeeks.org/problems/delete-middle-element-of-a-stack/1

'''

class Solution:
    def recursion(self, s, l, sizeOfStack):
        if not s or l == sizeOfStack:
            return
            
        temp = s.pop()
        
        self.recursion(s, l+1, sizeOfStack)
        if l != int(sizeOfStack/2):
            s.append(temp)
            
       
    def deleteMid(self, s, sizeOfStack):
        return self.recursion(s, 0, sizeOfStack)
       

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()
    
