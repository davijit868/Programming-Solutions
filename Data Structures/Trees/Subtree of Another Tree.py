'''

Problem 572 | Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        node = root
        
        def is_same(r, sr):
            if not r and not sr:
                return True
            elif not r or not sr:
                return False
            elif r and sr:
                if r.val != sr.val:
                    return False
                else:
                    return is_same(r.left, sr.left) and is_same(r.right, sr.right)
        
        def traverse(node):
            if is_same(node, subRoot):
                return True
            left = right = False
            if node.left:
                left = traverse(node.left)
            if node.right:
                right = traverse(node.right)
            return left or right
        
        if traverse(root):
            return True
        else:
            return False
    
