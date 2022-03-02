'''

Problem 2 | Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ''
        while l1:
            first = str(l1.val) + first
            l1 = l1.next
        
        second = ''
        while l2:
            second = str(l2.val) + second
            l2 = l2.next
       
        final = str(int(first) + int(second))
      
        head = None
        
        while final:
            num = final[0]
            final = final[1:]
            cur = ListNode(val = int(num), next = head)
            head = cur
            
        return head
      
        
