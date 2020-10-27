# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion 
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        # Recursion
        if root is None:
            return False 
        
        sum -= root.val
        if root.left is None and root.right is None:
            return sum == 0 
        
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
        
#Time: O(N)   
#Space:O(logN), worst case is O(N)


# Iterations
 class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # Iterations: DFS + Stack
        if root is None:
            return False
        
        currsum = sum - root.val
        path = [(root,currsum)]
        
        while path:
            node,currsum = path.pop()
            
            # comes to a leaf node but might have another leaf node because path is not empty  
            if node.left is None and node.right is None and currsum ==0:
                return True 
            if node.left is not None:
                path.append((node.left,currsum-node.left.val))
            if node.right is not None:
                path.append((node.right,currsum-node.right.val))
        
        return False 
        
 
            