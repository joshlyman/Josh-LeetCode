# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        self.maxAvg = 0
        self.helper(root)
        
        return self.maxAvg 
    
    # node's num and node's val can be repeated by recursion 
    
    def helper(self,node):
        if not node:
            return [0,0]

        nodeNum1,nodeVal1 = self.helper(node.left)
        nodeNum2,nodeVal2 = self.helper(node.right)
        
        nodeNum = nodeNum1 + nodeNum2 + 1
        nodeVal = nodeVal1 + nodeVal2 + node.val 
        
        self.maxAvg = max(self.maxAvg,nodeVal/nodeNum)

        return [nodeNum,nodeVal]
    
     
# Time: O(N)
# Space:O(H)