'''

https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

'''

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:            
    def flatten(self, head: 'Node') -> 'Node':
        def get_tail(node):
            if node.child == None and node.next == None:
                return node
            elif node.child == None and node.next != None:
                return get_tail(node.next)
            elif node.child != None and node.next == None:
                node.next = node.child
                node.child.prev = node
                node.child = None
                return get_tail(node.next)
            elif node.child != None and node.next != None:
                _next = node.next
                node.next = node.child
                node.next.prev = node
                node.child = None
                node = get_tail(node.next)
                node.next = _next
                node.next.prev = node
                return get_tail(node.next)
        if head:        
            get_tail(head)
        return head
        
