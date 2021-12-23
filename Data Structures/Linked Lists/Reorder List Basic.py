'''

Problem 143 | Reorder List Basic Solution
https://leetcode.com/problems/reorder-list/

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        end = None
        def find_end():
            node = head
            while node.next.next:
                node = node.next
            end = copy.copy(node.next)
            node.next = None
            return end
        
        while curr:
            if curr.next:
                end = find_end()
                temp = curr.next
                curr.next = end
                end.next = temp
                curr = temp
            else:
                break

        return head
      
