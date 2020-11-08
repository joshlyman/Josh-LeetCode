# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion 
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val+=t2.val 
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        
        return t1

# Time: O(N), Here, m represents the minimum number of nodes from the two given trees.
# Space:O(N), average will be O(logM)

# Iterative 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        
        if not t2:
            return t1
        
        stack = [(t1,t2)]
        
        while stack:
            nt = stack.pop()
            
            if not nt[0] or not nt[1]:
                continue 
            
            nt[0].val += nt[1].val
        
            if not nt[0].left:
                nt[0].left = nt[1].left
            else:
                stack.append((nt[0].left,nt[1].left))
            
            if not nt[0].right:
                nt[0].right = nt[1].right
            else:
                stack.append((nt[0].right,nt[1].right))
            
        return t1

# Time: O(N)
# Space:O(N)