# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion 
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        return self.validBST(root,-inf,inf)
        

    def validBST(self,root,min,max):
         
        if root is None:
            return True 
        
        if root.val <= min or root.val >= max:
            return False
        

        # BFS: check each left and right child or leaf (no child) node every time 

        # upper bound for left node is val of node 
        # lower bound for right node is val of node
        return self.validBST(root.left,min,root.val) and self.validBST(root.right,root.val,max) 
        
# Time: O(n)
# Space: O(n), worst case if it is unbalanced. But if it is balanced, it will be O(h) or O(logN), where h is the height of tree 


# Iterative 
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True 
        
        stack = [(root,-math.inf, math.inf)]
        
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            
            val = root.val
            if val <= lower or val >= upper:
                return False
            
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True 
        
