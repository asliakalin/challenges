"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0: return None
        root = TreeNode(postorder[-1])  
        if len(inorder) == 1: return root
        l, r = self.cutlist(inorder, postorder[:-1], root.val)
        root.right = self.buildTree(r[0], r[1])
        root.left = self.buildTree(l[0], l[1])
        return root
    
    
    def cutlist(self, inorder, post, val):
        left = [[],[]]
        right = [[],[]]
        split = ""
        for i in range(len(inorder)):
            if inorder[i] == val:
                left[0], right[0] = inorder[:i], inorder[i+1:]
                if i == len(inorder)-1: split = "No right subtree"
                elif i == 0: split = "No left subtree"
                else: split = set(inorder[i+1:]) #all right subtree mems
                break;
        if split == "No right subtree":
            left[1], right[1] = post, []
        elif split == "No left subtree":
            left[1], right[1] = [], post
        else:
            for i in range(len(post)):
                if set(post[i:]) == split:
                    left[1], right[1] = post[:i], post[i:]
            
        return left, right