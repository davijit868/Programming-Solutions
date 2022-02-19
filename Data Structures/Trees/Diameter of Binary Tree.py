'''

Problem 543 | Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0
        def height(node):
            nonlocal dia
            if node:
                l = height(node.left)
                r = height(node.right)
                if l + r > dia:
                    dia = l + r
                return 1 + max(l, r)
            else:
                return 0  
        height(root) 
        return dia
                         
