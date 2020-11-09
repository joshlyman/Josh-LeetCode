# DFS 

# recursion 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        
        def dfs(node,level,count):
            
            if level not in count:
                count[level] = []
                count[level].append(node.val)
            else:
                count[level].append(node.val)
            
            if node.left:
                dfs(node.left,level+1,self.count)
            
            if node.right:
                dfs(node.right,level+1,self.count)
            
        
        self.count = {}
        dfs(root,0,self.count)
        
        return [sum(self.count[level])/len(self.count[level]) for level in self.count]
    
    
# Time: O(M)
# Space:O(M)        
        
      


# BFS 

# iterative 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        
        count = {}
        queue = [(root,0)]
        
        while queue:
            node,level = queue.pop(0)
            
            if level not in count:
                count[level] = []
                count[level].append(node.val)
            else:
                count[level].append(node.val)
            
            if node.left:
                queue.append((node.left,level+1))
            
            if node.right:
                queue.append((node.right,level+1))
            
        return [sum(count[level])/len(count[level]) for level in count]

# Time: O(M)
# Space:O(M)
