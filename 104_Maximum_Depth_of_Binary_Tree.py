# recursion


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

# Time: O(n)
# Space:O(logn)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        else:
            left_height = 1+self.maxDepth(root.left)
            right_height = 1+self.maxDepth(root.right)
            
            return max(left_height,right_height)

# Time: O(n)
# Space:O(logn)
