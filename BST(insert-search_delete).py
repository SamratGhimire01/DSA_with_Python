class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value 
        
def insert(root,value):
    if root == None:
        return Node(value)
    if root.data == value:
        return root
    if root.data>value:
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root

def search(root,value):
    if root == None:
        print("Not Found",end='\n')
        return
    if root.data == value:
        print("Element Found",end='\n')
        return root
    if root.data>value:
        search(root.left,value)
    else:
        search(root.right,value)
    return root

def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
    return None
    
root = insert(None,20)
root = insert(root,43)
root = insert(root,22)
root = insert(root,66)
root = insert(root,77)
root = insert(root,99)
root = insert(root,35)

inorder(root)
search(root,55)
search(root,99)