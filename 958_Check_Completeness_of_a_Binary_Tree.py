# refer from:
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solution/

# 1.BFS 

# If we have say, 4 nodes in a row with depth 3 and positions 0, 1, 2, 3; and we want 8 new nodes 
# in a row with depth 4 and positions 0, 1, 2, 3, 4, 5, 6, 7; then we can see that the rule for 
# going from a node to its left child is (depth, position) -> (depth + 1, position * 2), and the 
# rule for going from a node to its right child is (depth, position) -> (depth + 1, position * 2 + 1).

# Then, our row at depth dd is completely filled if it has 2^{d-1} nodes, and all the nodes in the 
# last level are left-justified when their positions take the form 0, 1, ... in sequence with no gaps.





# 2. Iterative Morris traversal  
class Solution:
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # Handle the null scenario
        if not root:
            return None
        
        node = root
        while node:
            
            # If the node has a left child
            if node.left:
                
                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            
            # move on to the right side of the tree
            node = node.right

# Time: O(N)
# Space:O(1)          

# 3.Use reversed preorder traversal 
# find rightmost node first, then back to left from bottom to top
# preorder is root -> left -> right, here is right -> left -> root 

def __init__(self):
    self.prev = None
    
def flatten(self, root):
    if not root:
        return None
    self.flatten(root.right)
    self.flatten(root.left)
    
    root.right = self.prev
    root.left = None
    self.prev = root



# Time: O(N)
# Space:O(1)