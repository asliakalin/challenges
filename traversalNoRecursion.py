# Implement an inorder traversal without recursion. Nodes do not contain parent references

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        


def inorderTraversal(root):
    res = []
    if not root:
        return res
     
    stack = [root]
    
    while stack:
        node = stack.pop()
        curr = node
        while curr.left:
            stack.append(curr)
            curr = curr.left
        
        res.append(curr.val)
        #print(res)
        if curr.right:
            stack.append(curr.right)
        else:
            
        
        
    return res
    

root = Node(1)
Node1 = Node(2)
Node5 = Node(5)
root.left = Node1
root.right = Node5

print(inorderTraversal(root))
    
    
