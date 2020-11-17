# preorder: root -> left -> right
# inorder: left -> root -> right 
        
# we can first pick up root from preorder, then get the left and right subtrees from inorder


# Recursion 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # preorder: root -> left -> right
        # inorder: left -> root -> right 
        if not inorder:
            return 
        
        # if inorder:
            
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])

        return root

# V2

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(in_left = 0, in_right = len(inorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None
            
            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion 
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root
        
        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper()


# V3
class Solution(object):
    def buildTree(self, preorder, inorder):
        inorder_map = {val: i for i, val in enumerate(inorder)}
        return self.dfs_helper(inorder_map, preorder, 0, len(inorder) - 1)
    
    
    def dfs_helper(self, inorder_map, preorder, left, right):
        if not preorder : 
        	return
        node = preorder.pop(0)
        root = TreeNode(node)
        root_index = inorder_map[node]
        if root_index != left:
            root.left = self.dfs_helper(inorder_map, preorder, left, root_index - 1)
        if root_index != right:
            root.right = self.dfs_helper(inorder_map, preorder, root_index + 1, right)
        return root

# Time: O(N)
# Space;O(N)
