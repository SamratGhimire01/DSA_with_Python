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
        return "Not Found"
    if root.data == value:
        return "Founded"
    
    if root.data > value:
        return search(root.left,value)
    else:
        return search(root.right,value)

def get_successor(root):
    root = root.right
    while (root != None and root.left != None):
        root = root.left
    return root
    
def delete(root,value):
    if root == None:
        return root
    if root.data > value:
        root.left = delete(root.left,value)
    elif root.data < value:
        root.right = delete(root.right,value)
    else:
        if root.left == None:
            return root.right
        if root.right == None:
            return root.left
        else:
            succ = get_successor(root)
            root.data = succ.data
            root.right = delete(root.right,succ.data)
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
print(search(root,99))
print(search(root,700))

delete(root,77)
print('\n')
inorder(root)