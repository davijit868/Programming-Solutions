'''

https://leetcode.com/problems/odd-even-linked-list/
Problem 328 | Odd Even Linked List

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_head = None
        even_curr = None
        curr = head
        prev = ListNode(None, next=curr)
        idx = 1
        while prev.next:
            if idx % 2 == 0:
                temp = deepcopy(curr)
                if even_head:
                    even_curr.next = temp
                    even_curr = even_curr.next
                    even_curr.next = None
                else:
                    even_head = temp
                    even_head.next = None
                    even_curr = even_head
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
            idx += 1
        prev.next = even_head
        return head
                
        
