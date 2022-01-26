'''

Problem 876 | Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head 
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            if not fast:
                break      
        return slow
      
