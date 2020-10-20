
# 1. inorder traversal and find it 
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        def inorder(r:TreeNode):  
            if r is None: 
                return []
            else:
                
                rleft = inorder(r.left)
                right = inorder(r.right)
                
                return rleft + [r.val] + right
        
        
        travelist = inorder(root)
        closenodevalue = min(travelist,key=lambda x:abs(x-target))
        
        return closenodevalue 

# Time: O(N)
# Space:O(N)


# 2. no need to traversal all, stop when found 
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
	stack,pred = [], float('-inf')
                
        while stack or root:
            
            # go left as far as you can and add all nodes on the way into stack.
            while root:
                stack.append(root)
                root = root.left 
            root = stack.pop()
            
            # usually min value must be between previous node and current 
            if pred <= target and target <root.val:
                return min(pred,root.val,key=lambda x: abs(target-x))
            
            pred = root.val
            root = root.right 
        
        # if finally still not found, then predecessor is the one 
        return pred

# Time: O(K): average case. k is an index of closest element.worst cases: O(H+K) 

# It's known that average case is a balanced tree, in that case stack always contains a few elements,  
# and hence one does 2k operations to go to kth element in inorder traversal 
# (k times to push into stack and then k times to pop out of stack). That results in O(k) time complexity. 
# The worst case is a completely unbalanced tree, then you first push H elements into stack and then pop out k elements, that results in 
# O(H+k) time complexity.

# Space:O(H), up to O(H) to keep the stack in the case of non-balanced tree.


# 3. Binary search 
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
		r = root.val
	    while root:
	        if abs(root.val - target) < abs(r - target):
	            r = root.val
	        
	        # if smaller than root, go left, ow, go right 
	        if target < root.val:
	            root = root.left 
	        else:
	            root = root.right
	    return r

# Time: O(H) since here one goes from root down to a leaf.
# Space:O(1)





