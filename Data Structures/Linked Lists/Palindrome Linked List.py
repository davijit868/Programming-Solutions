'''

Problem 234 | Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = copy.deepcopy(head)
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        first = head
        while prev:
            if prev.val != first.val:
                return False
            prev = prev.next
            first = first.next
        return True
            
