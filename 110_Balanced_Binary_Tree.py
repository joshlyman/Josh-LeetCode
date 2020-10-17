# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def getheight(root):
            if root is None:
                return 0
            
            left_height, right_height = getheight(root.left),getheight(root.right)
            
            if left_height < 0 or right_height <0 or abs(left_height-right_height)>1:
                return -1
            
            return max(left_height,right_height)+1
        
        h = getheight(root)
        
        return (h>=0)

# Time: O(n), For every subtree, we compute its height in constant time as well as compare the height of its children.
# Space:O(n), The recursion stack may go up to O(n) if the tree is unbalanced.