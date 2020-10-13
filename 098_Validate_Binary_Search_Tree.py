# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        return self.validBST(root,-inf,inf)
        
        
    def validBST(self,root,min,max):
         
        if root is None:
            return True 
        
        if root.val <= min or root.val >= max:
            return False
        
        # upper bound for left node is val of node 
        # lower bound for right node is val of node
        return self.validBST(root.left,min,root.val) and self.validBST(root.right,root.val,max) 
        
# Time: O(n)
# Space: O(n)     
