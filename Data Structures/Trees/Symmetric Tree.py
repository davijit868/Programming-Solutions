'''

https://leetcode.com/problems/symmetric-tree/

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.is_mirror(root.left, root.right)

    def is_mirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            out_pair = self.is_mirror(left.left, right.right)
            in_pair = self.is_mirror(left.right, right.left)
            return out_pair and in_pair
        else:
            return False
