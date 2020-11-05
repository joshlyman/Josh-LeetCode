# refer from:
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solution/

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