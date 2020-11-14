# Recursive

# Start traversing the tree from the root node.
# If both the nodes p and q are in the right subtree, then continue the search with right subtree starting step 1.
# If both the nodes p and q are in the left subtree, then continue the search with left subtree starting step 1.
# If both step 2 and step 3 are not true, this means we have found the node which is common to node p's and q's subtrees. 
# and hence we return this common node as the LCA.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val = root.val 
        
        p_val = p.val
        q_val = q.val
        
        # if both p and q are greater than parent, means they are on right subtree
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right,p,q)
        # both are on the left subtree
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        else:
            return root

# Time: O(N)
# Space:O(N)


# Iterative 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        p_val = p.val
        q_val = q.val
        
        node = root 
        while node:
            
            parent_val = node.val 
            
            if p_val > parent_val and q_val > parent_val:  
                # If both p and q are greater than parent
                node = node.right 
            elif p_val < parent_val and q_val < parent_val: 
                # If both p and q are less than parent
                node = node.left 
            else:
                # We have found the split point, i.e. the LCA node.
                return node 


# Time: O(N)
# Space:O(1)
           
            
