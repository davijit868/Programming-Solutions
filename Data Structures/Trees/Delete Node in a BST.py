'''

Problem 450 | Delete Node in a BST
https://leetcode.com/problems/delete-node-in-a-bst/

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else: 
                root.val = self.predesessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
    
    def successor(self, root: TreeNode) -> TreeNode:
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predesessor(self, root: TreeNode) -> TreeNode:
        root = root.left
        while root.right:
            root = root.right
        return root.val
    
