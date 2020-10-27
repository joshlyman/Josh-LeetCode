# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1: Recursion 
# DFS 
# left -> node -> right 
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        res = []
        self.dfs(root,res)
        return res 
        
    def dfs(self,root,res):
        
        if root is not None:
            if root.left is not None:
                self.dfs(root.left,res)
            
            res.append(root.val)
            
            if root.right is not None:
                self.dfs(root.right,res)
            
# Time: O(N)
# The recursive function is T(n) = 2 T(n/2)+1

# Space:O(N)
# The worst case space required is O(n), 
# and in the average case it is O(logn) where n is number of nodes.

# Approach 2: Iterative 
# use stack 

# initialize the stack
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []
        # initialize the traveral list
        traversal = []
        
        # while we're at a valid node or there are
        # still nodes to traverse... 
        while stack or root:
            
            if root:
                # if we're at a valid node,
                # remember where we've been and keep moving left
                stack.append(root)
                root = root.left
            
            else:
                # otherwise we've hit a dead end so
                # -- pop the most recent value
                # -- report out
                # -- move right
                root = stack.pop()
                traversal.append(root.val)
                root = root.right
        
        return traversal

# Time: O(N)
# Space:O(N)


# Approach 3: Morris Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/solution/ 

# Refer from 
# https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/668448/Morris-Traversal

def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        while root:
            if not root.left: # if we don't have a left, this is our best in-order value at the moment. add it to the list and move right.
                res.append(root.val)
                root = root.right
            else:
                pred = self.findPredecessor(root) # find the predecessor for the given node. This is the farthest right of the first left we see.

                # if we have a right we have move on to explore this sub tree. The pred.right != root check is to ensure that we're not ex
                if pred.right != root:
                    pred.right = root
                    root = root.left
                else: 
                # otherwise, we have found a pointer back to the current root and we need to rewrite the tree structure. This is basically a form of "have we seen this before?".
                    root.left = None

        return res

    def findPredecessor(self, root: TreeNode) -> TreeNode:
        curr = root.left

        while curr.right and curr.right != root:
            curr = curr.right

        return curr


# Time complexity : O(n). 

# To prove that the time complexity is O(n), the biggest problem lies in finding the time complexity of finding the predecessor nodes of all the nodes 
# in the binary tree. Intuitively, the complexity is O(nlogn), because to find the predecessor node for a single node related to the height of the tree. 
# But in fact, finding the predecessor nodes for all nodes only needs O(n) time. Because a binary Tree with n nodes has n-1n−1 edges, 
# the whole processing for each edges up to 2 times, one is to locate a node, and the other is to find the predecessor node. So the complexity is O(n).

# Space complexity : O(n). Arraylist of size n is used.




