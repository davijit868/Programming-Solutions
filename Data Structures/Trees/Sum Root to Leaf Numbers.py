'''

https://leetcode.com/problems/sum-root-to-leaf-numbers/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorder(self, node, current_path, all_path):
        if node:
            current_path += str(node.val)
            if node.left == None and node.right == None:
                all_path.append(current_path)
            self.preorder(node.left, current_path, all_path)
            self.preorder(node.right, current_path, all_path)
            
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        current_path = ""
        all_path = []
        self.preorder(root, current_path, all_path)
        total = 0
        for i in all_path:
            total += int(i)
        return total
