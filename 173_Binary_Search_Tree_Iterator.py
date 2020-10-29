# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Refer from:
# https://leetcode.com/problems/binary-search-tree-iterator/solution/

# Approach 1: Flatten BST using inorder traversal to get the new sorted array
class BSTIterator:

    def __init__(self, root: TreeNode):
        
        # contain all the nodes from inorder traversal in an array
        self.sorted_nodes = []
        
        # start from -1 index, then go to next smallest element in array
        self.index = -1
        
        # call inorder traversal to put all nodes in array
        self.inorder(root)
    
    def inorder(self,root):
        if root is None:
            return None
        
        self.inorder(root.left)
        self.sorted_nodes.append(root.val)
        self.inorder(root.right)
    
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        self.index+=1
        return self.sorted_nodes[self.index]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.index + 1 < len(self.sorted_nodes):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Time: O(N) is the time taken by the constructor for the iterator. 
# The problem statement only asks us to analyze the complexity of the two functions, 
# however, when implementing a class, it's important to also note the time it takes to initialize a new object of the class 
# and in this case it would be linear in terms of the number of nodes in the BST. 
# In addition to the space occupied by the new array we initialized, the recursion stack for the inorder traversal also occupies space but that 
# is limited to O(h) where h is the height of the tree.

# next() would take O(1)
# hasNext() would take O(1)

# Space: O(N) since we create a new array to contain all the nodes of the BST. 
# This doesn't comply with the requirement specified in the problem statement that the maximum space 
# complexity of either of the functions should be O(h) where 
# h is the height of the tree and for a well balanced BST, the height is usually logN. 
# So, we get great time complexities but we had to compromise on the space. 
# Note that the new array is used for both the function calls and hence the space complexity for both the calls is O(N).

# Approach 2: Controlled Recursion by using custom stack, each time pop out node when calling next function. 
class BSTIterator:
    def __init__(self, root: TreeNode):
            
        self.stack = []
        
        self.leftmost_inorder(root)

    def leftmost_inorder(self,root):
        # For a given node, add all the elements in the leftmost branch of the tree under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left
            
            
    def next(self) -> int:
        
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()
        
        if topmost_node.right: 
            self.leftmost_inorder(topmost_node.right)
        return topmost_node.val 
    
    def hasNext(self) -> bool:
        return len(self.stack)>0

# Time: O(N)

# hasNext is the easier of the lot since all we do in this is to return true if there are any elements left in the stack. 
# Otherwise, we return false. So clearly, this is an O(1)O(1) operation every time. 
# Let's look at the more complicated function now to see if we satisfy all the requirements 
# in the problem statement

# next involves two major operations. One is where we pop an element from the stack which becomes the next smallest element to return. 
# This is a O(1) operation. However, we then make a call to our helper function _inorder_left which iterates over a bunch of nodes. 
# This is clearly a linear time operation i.e. O(N) in the worst case. This is true.

# However, the important thing to note here is that we only make such a call for nodes which have a right child. 
# Otherwise, we simply return. Also, even if we end up calling the helper function, 
# it won't always process N nodes. They will be much lesser. Only if we have a skewed tree would there be N nodes for the root. 
# But that is the only node for which we would call the helper function.

# Thus, the amortized (average) time complexity for this function would still be O(1) which is what the question asks for. 
# We don't need to have a solution which gives constant time operations for every call. We need that complexity on average and 
# that is what we get.

# Space:O(h) 

# The space complexity is O(h) which is occupied by our custom stack for simulating the inorder traversal. 
# Again, we satisfy the space requirements as well as specified in the problem statement.










