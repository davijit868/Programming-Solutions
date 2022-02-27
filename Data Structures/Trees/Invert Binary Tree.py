'''

Problem 226 | Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        def invert(node):
            if node:
                if node.left or node.right:
                    temp = node.right
                    node.right = node.left
                    node.left = temp
                invert(node.left)
                invert(node.right)
        invert(node)
        return root
      
