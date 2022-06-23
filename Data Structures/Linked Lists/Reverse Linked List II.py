'''

Problem 92 | Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head.next:
            return head
        
        curr, start = head, head
        
        count = 1
        
        while count < left:
            start = curr
            curr = curr.next
            count += 1
            
        tail = curr
        
        prev = None
        while count < right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1
            
        last = curr.next
        curr.next = prev
        prev = curr
        start.next = curr
        tail.next = last
        
        if left > 1:
            return head
        
        return prev
        
