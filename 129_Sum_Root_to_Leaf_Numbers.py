# preorder 

# iterative using stack 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        root_to_leaf = 0
        stack = [(root,0)]
        
        while stack:
            root,curr_number = stack.pop()
            
            if root is not None:
                curr_number = curr_number*10+root.val 
            
                # if it's a leaf, update root-to-leaf sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number

                else:

                	# put right first, then put left 
                    stack.append((root.right,curr_number))
                    stack.append((root.left,curr_number))
        
        return root_to_leaf 

# Time: O(N)
# Space:O(H)

# recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        self.root_to_leaf = 0
        
        def preorder(node,curr_number): 
            
            if node is not None:
                curr_number = curr_number * 10 + node.val
                
                # reach to the leaf node 
                if node.left is None and node.right is None:
                    self.root_to_leaf += curr_number 
                
                preorder(node.left,curr_number)
                preorder(node.right,curr_number)
        
        preorder(root,0)
        
        return self.root_to_leaf 

# Time: O(N)
# Space:O(H)      