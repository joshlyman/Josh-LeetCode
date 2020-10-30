"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # Here the problem is to implement DFS inorder traversal in a textbook recursion way because of in-place requirement.
        
        if root is None:
            return None 
        
        # the smallest (first) and the largest (last) nodes
        
        self.first = None
        self.last = None
        
        # performs inorder traversal 
        # left -> node -> right 
        def helper(node):
            
            
            if node is not None:
                # recursion on left node
                helper(node.left)

                # if not the beginning node
                if self.last is not None:
                    # link previous node (last) with current node (node)

                    self.last.right = node
                    node.left = self.last
                else:

                    # if it is beginning node 
                    self.first = node

                # make current node be previous node 
                self.last = node

                # recursion on right node
                helper(node.right)
        
        
        helper(root)
        # finally link the last and first node together, close the loop
        self.last.right = self.first
        self.first.left = self.last
        
        return self.first 
            
                 
# Time: O(N)

# Space:O(N), We have to keep a recursion stack of the size of the tree height, 
# which is O(logN) for the best case of completely balanced tree 
# and O(N) for the worst case of completely unbalanced tree.
