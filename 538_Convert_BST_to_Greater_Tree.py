# Revesred in-order traversal 
# from right to root to left 

# The basic idea of such a traversal is that before visiting any node in the tree, we must first visit all nodes with greater value. 
# which is in right subtree 

# For the recursive approach, we maintain some minor "global" state so each recursive call can access and modify the current total sum. 
# Essentially, we ensure that the current node exists, recurse on the right subtree, visit the current node by updating its value 
# and the total sum, and finally recurse on the left subtree. 


# Recursion 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        # right -> root -> left 
        if root is not None:
            self.convertBST(root.right)
            self.total+= root.val 
            root.val = self.total 
            self.convertBST(root.left)
        return root 

# Time: O(N)
# Space:O(N)


# iterative using Stack 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0
        node = root
        stack = []
        
        # push all nodes up to (and including) this subtree's maximum on
        # the stack.
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right
        
            # pop start from rightmost 
            node = stack.pop()
            total+=node.val 
            node.val = total 
            
            # all nodes with values between the current and its parent lie in the left subtree.
            node = node.left
        return root 
 
 # Time: O(N)
 # Space:O(N) 




# refer from:
# https://leetcode.com/problems/convert-bst-to-greater-tree/solution/

# use constant space
# Reverse Morris in-order traversal 

# In general, the recursive and iterative stack methods sacrifice linear space for the ability to return 
# to a node after visiting its left subtree. The Morris traversal instead exploits the unused null pointer(s) 
# of the tree's leaves to create a temporary link out of the left subtree, allowing the traversal to be 
# performed using only constant additional memory. To apply it to this problem, we can simply swap all 
# "left" and "right" references, which will reverse the traversal.

class Solution(object):
    def convertBST(self, root):
        # Get the node with the smallest value greater than this one.
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ
                
        total = 0
        node = root
        while node is not None:
            # If there is no right subtree, then we can visit this node and
            # continue traversing left.
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            # If there is a right subtree, then there is a node that has a
            # greater value than the current one. therefore, we must traverse
            # that node first.
            else:
                succ = get_successor(node)
                # If there is no left subtree (or right subtree, because we are
                # in this branch of control flow), make a temporary connection
                # back to the current node.
                if succ.left is None:
                    succ.left = node
                    node = node.right
                # If there is a left subtree, it is a link that we created on
                # a previous pass, so we should unlink it and visit this node.
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        
        return root

# Time: O(N)
# Space:O(1)












        