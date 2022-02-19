'''

Problem 83 | Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

'''

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if node:
            while node.next:
                if node.val == node.next.val:
                    node.next = node.next.next
                else:
                    node = node.next
        return head
      
