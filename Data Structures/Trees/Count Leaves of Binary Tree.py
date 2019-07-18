
def countLeaves(root):
    if not root: return 0
    if not root.left and not root.right: return 1
    return countLeaves(root.left) + countLeaves(root.right)
        
