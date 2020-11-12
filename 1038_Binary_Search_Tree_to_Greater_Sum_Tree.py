# same with LC 538 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
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