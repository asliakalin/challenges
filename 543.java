/** 
Given a binary tree, you need to compute the length of the diameter of the tree. 
he diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
*/


class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {return 0;}
        else if (root.right == null && root.left == null) {
            return 0;
        } else {
            return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
        }
            
    }
    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) {return 0;}
        else if (root.right == null && root.left == null) {return 0;}
        else {
            return Math.max(Math.max(diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right)), maxDepth(root.left) + maxDepth(root.right) + ((root.right != null && root.left != null)? 2 : 1));
        }
    }
}

/// Runtime: 9 ms, faster than 13.90% of Java online submissions for Diameter of Binary Tree.
/// Memory Usage: 39.1 MB, less than 14.29% of Java online submissions for Diameter of Binary Tree.



class Solution {
    int ans;
    public int diameterOfBinaryTree(TreeNode root) {
        ans = 1;
        depth(root);
        return ans - 1;
    }
    public int depth(TreeNode node) {
        if (node == null) return 0;
        int L = depth(node.left);
        int R = depth(node.right);
        ans = Math.max(ans, L+R+1);
        return Math.max(L, R) + 1;
    }
}


/// Runtime: 0 ms, faster than 100.00% of Java online submissions for Diameter of Binary Tree.
/// Memory Usage: 38.9 MB, less than 14.86% of Java online submissions for Diameter of Binary Tree.


