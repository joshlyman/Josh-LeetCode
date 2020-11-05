# 1.BFS 

# If we have say, 4 nodes in a row with depth 3 and positions 0, 1, 2, 3; and we want 8 new nodes 
# in a row with depth 4 and positions 0, 1, 2, 3, 4, 5, 6, 7; then we can see that the rule for 
# going from a node to its left child is (depth, position) -> (depth + 1, position * 2), and the 
# rule for going from a node to its right child is (depth, position) -> (depth + 1, position * 2 + 1).

# Then, our row at depth dd is completely filled if it has 2^{d-1} nodes, and all the nodes in the 
# last level are left-justified when their positions take the form 0, 1, ... in sequence with no gaps.

# We can find the codes of every node in the tree in "reading order" (top to bottom, left to right) 
# sequence using a breadth first search. (We could also use a depth first search and sort the codes later.)

# Then, we check that the codes are the sequence 1, 2, 3, ... with no gaps. Actually, 
# we only need to check that the last code is correct, since the last code is the largest value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        # store node and # 
        nodes  = [(root,1)]
        
        i = 0
        while i <len(nodes):
            node,v = nodes[i]
            i+=1
            
            if node:
                nodes.append((node.left,2*v))
                nodes.append((node.right,2*v+1))
        
        # check if there is a gap in index or not 
        return nodes[-1][1] == len(nodes)

# Same but use queue 
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = collections.deque([(root, 1)])
        res = []
        while q:
            u, coord = q.popleft()
            res.append(coord)
            if u.left:
                q.append((u.left, 2*coord))
            if u.right:
                q.append((u.right, 2*coord+1))
        return len(res) == res[-1]

# Time: O(N)
# Space:O(N)



# 2. DFS
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # number of nodes, right_most_coords
        def dfs(root, coord):
            if not root:
                return 0, 0
            l = dfs(root.left, 2*coord)
            r = dfs(root.right, 2*coord+1)
            tot = l[0]+r[0]+1
            right_most = max(coord, l[1], r[1])
            return tot, right_most
        if not root:
            return True
        tot, right_most = dfs(root, 1)
        return tot == right_most

# Time: O(N)
# Space:O(H)