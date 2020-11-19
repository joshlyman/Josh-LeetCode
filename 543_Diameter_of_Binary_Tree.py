# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Diameter = 1+ max depth of left and max depth of right
# use DFS to recursively find left and right nodes 

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        
        def depth(p):
            if not p:
                return 0
            
            left = depth(p.left)
            right = depth(p.right)
            
            self.ans = max(self.ans,left+right+1)
            return max(left,right)+1
            
        depth(root)
        return self.ans-1


# Time: O(N), we visit every node once.
# Space:O(N). the size of our implicit call stack during our depth-first search.