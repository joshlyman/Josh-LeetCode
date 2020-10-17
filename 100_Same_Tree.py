# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not p and not q:
            return True 
        
        if not p or not q:
            return False
        
        if p.val!=q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
 
 # Time: O(n), where N is a number of nodes in the tree, since one visits each node exactly once.

 # Space:O(logn), in the best case of completely balanced tree and O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.