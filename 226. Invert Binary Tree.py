# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive 
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
        
        return root 

# Time: O(N)
# Space:O(H)       

# iterative 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                
                if node.left:   
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                node.left, node.right = node.right, node.left 
            
        return root 

# Time: O(N)
# Space:O(N)       
