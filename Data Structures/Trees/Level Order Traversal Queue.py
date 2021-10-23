'''

https://www.geeksforgeeks.org/level-order-tree-traversal/

'''

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
def print_level_order(root):
    queue = []
    if root:
        queue.append(root)
    while(len(queue)):
        current = queue.pop(0)
        print(current.data, sep="")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

root = Node(7)
root.left = Node(8)
root.right = Node(3)
root.left.left = Node(1)
root.left.right = Node(2)
 
print("Level order traversal of binary tree is: ")
print_level_order(root)
