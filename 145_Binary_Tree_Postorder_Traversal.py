# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        res = []
        self.dfs(root,res)
        return res
    
    def dfs(self,root,res):
        
        if root:
            if root.left is not None:
                self.dfs(root.left,res)
            if root.right is not None:
                self.dfs(root.right,res)
            res.append(root.val)
        
# Time: O(N)
# Space:O(N)  

# Iteration: Iterative Preorder Traversal: Tweak the Order of the Output
# preorder is node -> left -> right 
# so we can change the order in stack in preorder iterative to node -> right -> left, then if we tweek this ([::-1]), it becomes left -> right -> node 

class Solution(object):
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)

            # different with preorder that preorder is push right then push left because left is first, right is second 
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
                
        return output[::-1]

# Note that Postorder cannot use Morris traversal 


# Iteration II: Iterative Postorder Traversal
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, output = [], []
        while root or stack:
            # push nodes: right -> node -> left 
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            # if the right subtree is not yet processed
            if stack and root.right == stack[-1]:
                stack[-1] = root
                root = root.right
            # if we're on the leftmost leaf
            else:
                output.append(root.val)
                root = None
                
        return output
# Time: O(N)
# Space:O(N) 
        
        