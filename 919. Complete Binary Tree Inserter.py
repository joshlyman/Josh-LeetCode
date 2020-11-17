Store tree nodes to a list self.tree in bfs order.
Node tree[i] has left child tree[2 * i + 1] and tree[2 * i + 2]

So when insert the Nth node (0-indexed), we push it into the list.
we can find its parent tree[(N - 1) / 2] directly.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.tree = [root]
        for i in self.tree:
            if i.left:
                self.tree.append(i.left)
            if i.right:
                self.tree.append(i.right)

    def insert(self, v: int) -> int:
        N = len(self.tree)
        self.tree.append(TreeNode(v))
        
        # if N is odd, N%2 is 1, So index of new inserted node is N+1th, but in index it is Nth index. So still odd number, should be in the left  
        # left child of node i is 2i+1, and right child is 2i+2
        if N%2:
            self.tree[(N-1)//2].left = self.tree[-1]
        else:
            self.tree[(N-1)//2].right = self.tree[-1]
        
        # return parent node's value 
        return self.tree[(N-1)//2].val
    
    def get_root(self) -> TreeNode:
        return self.tree[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()

Time: O(N)
Space:O(N)