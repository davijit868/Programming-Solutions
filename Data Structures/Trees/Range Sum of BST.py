'''

Problem 938 | Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        node = root
        def inorder_traverse(node):
            nonlocal total
            if node:
                if node.val >= low and node.val <= high:
                    total += node.val
                if node.val > low:
                    inorder_traverse(node.left)
                if node.val < high:
                    inorder_traverse(node.right)
        inorder_traverse(node)
        return total
            
        
