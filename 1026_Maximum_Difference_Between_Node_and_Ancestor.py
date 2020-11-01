# Given any two nodes on the same root-to-leaf path, they must have the required ancestor relationship.
# Therefore, we just need to record the maximum and minimum values of all root-to-leaf paths and return the maximum difference.
# To achieve this, we can record the maximum and minimum values during the recursion and return the difference when encountering leaves.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root is None:
            return 0
    
        def helper(node,cur_max,cur_min):
            # if comes to child of leaf node, just return 
            if node is None:
                return cur_max - cur_min
            
           # else, update max and min
            # and return the max of left and right subtrees
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)
            
            return max(left, right)
        
        return helper(root,root.val,root.val)
  

# Time: O(N)

# Space:O(N), since we need stacks to do recursion, and the maximum depth of the recursion is the height of the tree, which is O(N) in the worst case 
# and O(log(N)) in the best case.
