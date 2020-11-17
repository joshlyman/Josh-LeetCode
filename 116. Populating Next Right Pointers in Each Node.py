# Refer from:
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/solution/

# Approach 1: level order traversal 

import collections 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # Initialize a queue data structure which contains
        # just the root of the tree
        Q = collections.deque([root])
        
        # Outer while loop which iterates over 
        # each level
        while Q:
            
            # Note the size of the queue
            size = len(Q)
            
            # Iterate over all the nodes on the current level
            for i in range(size):
                
                # Pop a node from the front of the queue
                node = Q.popleft()
                
                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only 
                # don't establish next pointers beyond the end
                # of a level

                # so this guarantee the last node of each level will not be assigned to the node in queue 
                if i < size - 1:
                    node.next = Q[0]
                
                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        # Since the tree has now been modified, return the root node
        return root

# Time: O(N)
# Space:O(N)


# Approach 2: Using previously established next pointers


# 1.This first case is the one where we establish the next pointers between the two children of a given node. This is the easier of the two cases since both the children are accessible via the same node. We can simply do the following to establish this connection.

 # node.left.next = node.right

# 2. This next case is not too straightforward to handle. In addition to establishing the next pointers between the nodes having a common parent, we also need to set-up the correct pointers between nodes which have a different parent.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        
        # we use leftmost to traversal each level, each level is like a linked list 
        leftmost = root
        
        # Once we reach the final level, we are done
        while leftmost.left:
            
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level

            # We need that node to start traversal on a particular level. 
            # Think of it as the head of the linked list. Since this is a perfect binary tree, 
            # the leftmost node will always be the left child of the current leftmost node. 
            # The only nodes which don't have any children are the ones on the final level and 
            # these would be the leaves of the tree.
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # Progress along the list (nodes on the current level)
                head = head.next
            
            # Move onto the next level
            leftmost = leftmost.left
        
        return root 
    
# Time: O(N)
# Space:O(1)




