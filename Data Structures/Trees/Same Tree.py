'''

Problem 100 | Same Tree
https://leetcode.com/problems/same-tree/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        first = p
        second = q
        
        def inorder_compare(first, second):
            if not first and not second:
                return True
            elif not first and second:
                return False
            elif first and not second:
                return False
            elif first.val == second.val:
                return inorder_compare(first.left, second.left) and \
                       inorder_compare(first.right, second.right)
            else:
                return False
        
        return inorder_compare(first, second)
        
