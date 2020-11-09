# DFS 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# recursion 
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def construct_paths(node,path):
            if not node:
                return 
        
            if node:
                path += str(node.val)

                # mean reach a leaf 
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path+='->'
                    construct_paths(node.left,path)
                    construct_paths(node.right,path)
        
        paths = []
        construct_paths(root,'')
        return paths

# Time: O(N)
# Space:O(N) for worst case(unbalanced tree), average is O(H) or O(logN)



# iterative
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        
        return paths

# Time: O(N) 
# Space:O(N)   