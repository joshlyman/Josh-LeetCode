# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # one needs to modify the above function and to check at each step what is better : to continue the current path or to start a new path with the current node as a highest node in this new path.
        
        self.max_path = float("-inf") # placeholder to be updated
 		
        def get_max_gain(node):
     		
            # nonlocal max_path # This tells that max_path is not a local variable
            if node is None:
                return 0
 				
            gain_on_left = max(get_max_gain(node.left), 0) # Read the part important observations
            gain_on_right = max(get_max_gain(node.right), 0)  # Read the part important observations
 			
            current_max_path = node.val + gain_on_left + gain_on_right # Read first three images of going down the recursion stack
            self.max_path = max(self.max_path, current_max_path) # Read first three images of going down the recursion stack
			
            return node.val + max(gain_on_left, gain_on_right) # Read the last image of going down the recursion stack
			
			
        get_max_gain(root) # Starts the recursion chain
        return self.max_path		

# Time: O(N)
# Space:O(H)