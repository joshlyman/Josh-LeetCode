# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        # different with 104 maximum depth of tree here. 
        if root.left == None:
            return 1+ self.minDepth(root.right)
        elif root.right == None:
            return 1+ self.minDepth(root.left)
        else:
            left_height = 1 + self.minDepth(root.left)
            right_height = 1 + self.minDepth(root.right)
            
            return min(left_height,right_height)

# Time: O(n)
# Space:O(log(n)), worst case: O(n)

# in the worst case, the tree is completely unbalanced, e.g. 
# each node has only one child node, the recursion call would occur N times 
# (the height of the tree), therefore the storage to keep the call stack would be O(n). 
# But in the best case (the tree is completely balanced), the height of the tree would be O(logN). 
# Therefore, the space complexity in this case would be O(logN)


# BFS 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = collections.deque([(root, 1)])
        
        while queue:
            node,depth = queue.popleft()
    
            if not node.left and not node.right:
                return depth 
            
            if node.left:
                queue.append((node.left, depth+1))
            
            if node.right:
                queue.append((node.right, depth+1))
            
# Time: O(N)
# Space:O(N)            
            
        
            
