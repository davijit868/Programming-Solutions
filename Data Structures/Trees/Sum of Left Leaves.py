'''

https://leetcode.com/problems/sum-of-left-leaves/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        total = self.inorder(root, total)
        return total
    
    def inorder(self, node, total):
        if (node.left != None) and (node.left.left == None) and (node.left.right == None):
            total += node.left.val
        if node.left:
            total = self.inorder(node.left, total)
        if node.right:
            total = self.inorder(node.right, total)
        return total
        
