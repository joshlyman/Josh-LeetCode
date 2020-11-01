# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# offical solution:
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/solution/


# This question requires to output nodes from top to bottom and left to right
# In BFS, we dont need to consider sorted by row because BFS is from top to bottom
# But in DFS, we have to consider sorted by row becauee DFS start from bottom 

# BFS 
# 1.record column and node both when doing BFS 
# 2.put nodes for each column in hash table 
# 3.sort column hash table and output each column's nodes list 

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        columnTable = collections.defaultdict(list)
        queue = collections.deque([(root,0)])
        
        while queue:
            node,column = queue.popleft()
        
            if node is None:
                continue
            
            columnTable[column].append(node.val)
            
            queue.append([node.left,column-1])
            queue.append([node.right,column+1])
        
        return [columnTable[i] for i in sorted(columnTable)]
            
# Time: O(NlogN), where N is the number of nodes in the tree.

# In the first part of the algorithm, we do the BFS traversal, whose time complexity is O(N) since we traversed each node once and only once.
# In the second part, in order to return the ordered results, we then sort the obtained hash table by its keys, which could result in the O(NlogN) time complexity in the worst case scenario where the binary tree is extremely imbalanced (for instance, each node has only left child node.)
# As a result, the overall time complexity of the algorithm would be O(NlogN).

# Space:O(N)            

# First of all, we use a hash table to group the nodes with the same column index. The hash table consists of keys and values. In any case, the values would consume O(N) memory. While the space for the keys could vary, in the worst case, each node has a unique column index, i.e. there would be as many keys as the values. Hence, the total space complexity for the hash table would still be O(N).
# During the BFS traversal, we use a queue data structure to keep track of the next nodes to visit. At any given moment, the queue would hold no more two levels of nodes. For a binary tree, the maximum number of nodes at a level would be (N+1)/2, which is also the number of leafs in a full binary tree. As a result, in the worst case, our queue would consume at most O(N+1)/2 *2 =O(N) space.
# Lastly, we also need some space to hold the results, which is basically a reordered hash table of size O(N) as we discussed before.


# BFS wo sorting
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return [] 
            
        columnTable = collections.defaultdict(list)
        queue = collections.deque([(root,0)])
        min_col = 0
        max_col = 0
        
        while queue:
            node,column = queue.popleft()

            if node is None:
                continue

            columnTable[column].append(node.val)
            
            min_col = min(min_col,column)
            max_col = max(max_col,column)

            queue.append([node.left,column-1])
            queue.append([node.right,column+1])

        # Here we replace sorted dict with the min and max so decrease time to O(N)
        return [columnTable[i] for i in range(min_col,max_col+1)]

# Time: O(N)
# Space:O(N)

# DFS
# any traversal will be fine
# need to sort row, this is different with BFS
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        # DFS by recursion  
        if root is None:
            return []

        columnTable = collections.defaultdict(list)
        min_col = max_col = 0
        
        def dfs(node,row,column):
            if node is not None:
                
                # this will be inorder DFS
                # dfs(node.left, row + 1, column - 1)

                nonlocal min_col, max_col
                columnTable[column].append((row,node.val))
                min_col = min(min_col, column)
                max_col = max(max_col, column)

                # preorder DFS, 
                dfs(node.left, row + 1, column - 1)
                dfs(node.right, row + 1, column + 1)

        dfs(root,0,0)
        
        res = []
        for col in range(min_col,max_col+1):
            columnTable[col].sort(key=lambda x:x[0])
            colVals = [val for row,val in columnTable[col]]
            res.append(colVals)
        
        return res 

# Time: O(W*HlogH)    
# Space:O(N)    
        