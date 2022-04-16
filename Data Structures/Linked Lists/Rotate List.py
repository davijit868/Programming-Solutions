'''

Problem 61 | Rotate List
https://leetcode.com/problems/rotate-list/

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
       
        if l > 1:
            for i in range(k%l):
                node = head
                prev = None
                while node.next:
                    prev = node
                    node = node.next
                node.next = head
                prev.next = None
                head = node
        return head
            
