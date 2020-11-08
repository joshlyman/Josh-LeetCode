# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        
        # count how many nodes 
        self.res = 0
        
        def find(node):
            if not node: 
                return float('inf'), float('-inf'), 0
            
            lmin, lmax, lnum = find(node.left)
            rmin, rmax, rnum = find(node.right)
            n = float('-inf')
            
            # the subtree must satisfy bst condition
            # which is larger than the max value of left and smaller than the min value of right 
            if node.val > lmax and node.val < rmin:
                
                # node number is left + right + node itself 
                n = lnum + rnum + 1
                
                # update current max subtree 
                self.res = max(n, self.res)
            
            return min(node.val, lmin), max(node.val, rmax), n
        
        find(root)
        return self.res

# Time: O(N)
# Space:O(H)