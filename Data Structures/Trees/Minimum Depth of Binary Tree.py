'''

Problem 111 | Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        node = root
        height = 1
        def depth(node, height):
            # print(node)
            if not node.left and not node.right:
                return height
            elif not node.left and node.right:
                return depth(node.right, 1 + height)
            elif node.left and not node.right:
                return depth(node.left, 1 + height)
            else:
                return min(depth(node.left, 1 + height), depth(node.right, 1 + height))
        if root:
            return depth(root, height)
        else:
            return 0
        
