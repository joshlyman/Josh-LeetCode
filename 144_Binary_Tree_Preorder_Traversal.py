# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1: iterations 
# preorder use DFS
# top -> bottom -> left -> right
# use stack so last in first out 

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return []
        
        # Let's start from the root and then at each iteration pop the current node out of the stack and push its child nodes. In the implemented strategy we push nodes into output list following the order Top->Bottom and Left->Right, that naturally reproduces preorder traversal.
        stack = [root]
        output = []
        
        while stack:
            root = stack.pop()
            
            if root is not None:
                output.append(root.val)
                # In stack, last in first out, so if we push right node first, right is processsd in the last. we push left last, so left is done first.
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return output 

# Time: O(N)
# we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes, i.e. the size of tree.

# Space:O(N)
# depending on the tree structure, we could keep up to the entire tree, therefore, the space complexity is O(N).
# best is O(logN)


# Approach 3: recursion 
def preorderTraversal(self, root):
    res = []
    self.dfs(root, res)
    return res
    
def dfs(self, root, res):
    if root:
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)



# Approach 2: Morris traversal
# no need to use stack 


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node, output = root, []
        while node:  
            if not node.left: 
                output.append(node.val)
                node = node.right 
            else: 
                current = node.left 

                while current.right and current.right is not node: 
                    current = current.right 

                if not current.right:
                    output.append(node.val)
                    current.right = node  
                    node = node.left  
                else:
                    current.right = None
                    node = node.right         

        return output

# Time : O(N) 
# we visit each predecessor exactly twice descending down from the node, 
# thus the time complexity is O(N), where N is the number of nodes, i.e. the size of tree.

# Space: O(N), 
# we use no additional memory for the computation itself, but output list contains N elements, 
# and thus space complexity is O(N).




