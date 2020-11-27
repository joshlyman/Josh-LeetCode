# Given a node in our tree, we know that it is a univalue subtree if it meets one of the following criteria:

# The node has no children (base case)
# All of the node's children are univalue subtrees, and the node and its children all have the same value



def countUnivalSubtrees(self, root):
    self.count = 0
    self.checkUni(root)
    return self.count

# bottom-up, first check the leaf nodes and count them, 
# then go up, if both children are "True" and root.val is 
# equal to both children's values if exist, then root node
# is uniValue suntree node. 
def checkUni(self, root):
    if not root:
        return True
    l, r = self.checkUni(root.left), self.checkUni(root.right)
    if l and r and (not root.left or root.left.val == root.val) and \
    (not root.right or root.right.val == root.val):
        self.count += 1
        return True
    return False


# Time: O(N)
# Space:O(H)