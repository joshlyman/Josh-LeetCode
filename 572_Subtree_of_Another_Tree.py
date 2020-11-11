# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        # if either one is empty, then false 
        if not s or not t: 
            return False
        
        # check root node 
        if self.isSameTree(s, t): 
            return True
        
        # check left and right node 
        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True 

    # base case for successive 
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # both are none 
        if not p and not q:
            return True
        
        # either is None 
        if not p or not q:
            return False
        
        # both are not none, then compare each root and subtree  
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Time: O(MN), A total of n nodes of the tree s and m nodes of tree t are traversed. 
# Space:O(N), The depth of the recursion tree can go upto n. n refers to the number of nodes in s.