'''

https://leetcode.com/problems/binary-tree-paths/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorder(self, node, current_path, all_path):
        if node:
            if current_path:
                current_path += "->" + str(node.val)
            else:
                current_path = str(node.val)
            if node.left == None and node.right == None:
                all_path.append(current_path)
            self.preorder(node.left, current_path, all_path)
            self.preorder(node.right, current_path, all_path)
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        current_path = ""
        all_path = []
        self.preorder(root, current_path, all_path)
        return all_path
        
