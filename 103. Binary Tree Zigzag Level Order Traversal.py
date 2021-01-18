# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # do BFS and if it is even level, reverse 
        
        if not root:
            return []
        
        queue = collections.deque()
        
        queue.append((root,1))
        
        d = collections.defaultdict(list)
        
        while queue:
            node,level = queue.popleft()
        
            d[level].append(node.val)
            
            if node.left:
                queue.append((node.left,level+1))
            
            if node.right:
                queue.append((node.right,level+1))
            
        res = []
        for level in d:
            if level%2 == 1:
                res.append(d[level])
            else:
                res.append(reversed(d[level]))
        
        return res 
        
# Time: O(N)
# Space:O(N)