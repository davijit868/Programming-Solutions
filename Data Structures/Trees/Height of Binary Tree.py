'''

https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

'''

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

maxHeight = 0
def height1(current):
    global maxHeight
    #print(current.info)
    if current.level > maxHeight:
        maxHeight = current.level
    if current.right:
        current.right.level = current.level + 1
        current = current.right
        height1(current)
    if current.left:
        current.left.level = current.level + 1
        current = current.left
        height1(current)

    return 
    

def height(root):
    root.level = 0
    height1(root)
    return maxHeight
