My solution: 

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        # To return a list of last elements from all levels, so it's the way more natural to implement BFS here. O(N) for both DFS and BFS, space: O(H) for DFS, O(D) for BFS, D is tree diameter. worst case are both O(N) (worst-case scenarios: skewed tree for DFS and complete tree for BFS.), so BFS win this problem 
        
        # BFS: 
        # step 1. push root into queue 
        # step 2. pop out a node from left 
        # step 3. Push the left child into the queue, and then push the right child.
        
        # DFS: to traverse the tree level by level, starting each time from the rightmost child. O(N), space is O(H)
        
        if root is None:
            return []
        
        rightside = []
        
        def helper(node:TreeNode,level:int) -> None:
            if level == len(rightside):
                rightside.append(node.val)
            
            for child in [node.right,node.left]:
                if child:
                    helper(child,level+1)
            
        helper(root,0)
        return rightside 

Time: O(N)
Space:O(H)


Other solutions refer from: https://leetcode.com/problems/binary-tree-right-side-view/discuss/56064/5-9-Lines-Python-48%2B-ms

Solution 1: Recursive, combine right and left: 5 lines, 56 ms

Compute the right view of both right and left left subtree, then combine them. For very unbalanced trees, this can be O(n^2), though.

def rightSideView(self, root):
    if not root:
        return []
    right = self.rightSideView(root.right)
    left = self.rightSideView(root.left)
    return [root.val] + right + left[len(right):]


Solution 2: Recursive, first come first serve: 9 lines, 48 ms

DFS-traverse the tree right-to-left, add values to the view whenever we first reach a new record depth. This is O(n).

def rightSideView(self, root):
    def collect(node, depth):
        if node:
            if depth == len(view):
                view.append(node.val)
            collect(node.right, depth+1)
            collect(node.left, depth+1)
    view = []
    collect(root, 0)
    return view

Solution 3: Iterative, level-by-level: 7 lines, 48 ms

Traverse the tree level by level and add the last value of each level to the view. This is O(n).

def rightSideView(self, root):
    view = []
    if root:
        level = [root]
        while level:
            view += level[-1].val,
            level = [kid for node in level for kid in (node.left, node.right) if kid]
    return view







