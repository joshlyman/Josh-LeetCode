# BFS
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        # BFS 
        if root is None:
            return []
        
        queue = collections.deque([(root,0)]) 
        rightside = []
        
        while queue:
            node,level = queue.pop()
            
            if level == len(rightside):
                rightside.append(node.val)
            
            if node.left:
                queue.append((node.left,level+1))
            
            if node.right:
                queue.append((node.right,level+1))
        
        return rightside
        
# Time: O(N)
# Space:O(D), D is diameter 

# DFS  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        # DFS
        rightside = []
        
        def helper(node,level):
            
            if node is None:
                return 
            
            if level == len(rightside):
                rightside.append(node.val)
            
            # first traversal right, then go left 
            if node.right:
                helper(node.right,level+1)
            
            if node.left:
                helper(node.left,level+1)
        
        helper(root,0)
        
        return rightside
        
# DFS V2
def rightSideView(self, root):
    if not root:
        return []
    right = self.rightSideView(root.right)
    left = self.rightSideView(root.left)
    return [root.val] + right + left[len(right):]


        
        
                
        
        
            
            
            
            
        
            
            
            
            