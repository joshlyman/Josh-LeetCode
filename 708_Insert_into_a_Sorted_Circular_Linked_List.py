# Refer solution:
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/solution/

# Two Pointers Iteration

# One of reasons of having two pointers rather than one is that in singly-linked list one does not have a reference to the precedent node, 
# therefore we keep an additional pointer which points to the precedent node. we iterate through the cyclic list 
# using two pointers, namely prev and curr. When we find a suitable place to insert the new value, we insert it between the prev and curr nodes.


# As we mentioned in the intuition, we loop over the linked list with two pointers (i.e. prev and curr) step by step. 
# The termination condition of the loop is that we get back to the starting point of the two pointers (i.e. prev == head)

# During the loop, at each step, we check if the current place bounded by the two pointers is 
# the right place to insert the new value.

# If not, we move both pointers one step forwards.

# Case 1). The value of new node sits between the minimal and maximal values of the current list. 
# As a result, it should be inserted within the list.

# Case 2). The value of new node goes beyond the minimal and maximal values of the current list, 
# either less than the minimal value or greater than the maximal value. In either case, 
# the new node should be added right after the tail node (i.e. the node with the maximal value of the list).

# Once we locate the tail and head nodes, we basically extend the original list by inserting the value in 
# between the tail and head nodes, i.e. in between the prev and curr pointers, the same operation as 
# in the Case 1.

# Case 3). Finally, there is one case that does not fall into any of the above two cases. 
# This is the case where the list contains uniform values.

# In this case, we would end up looping through the list and getting back to the starting point.

# The above three cases cover the scenarios within and after our iteration loop. There is 
# however one minor corner case we still need to deal with, where we have an empty list. 
# This, we could easily handle before the loop.


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        # if empty linked list 
        if head is None:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode
        
        prev,curr = head,head.next 
        toInsert = False 
        
        while True:
            if prev.val <= insertVal <= curr.val:
                # Case #1.
                toInsert = True
            elif prev.val > curr.val:
                # Case #2. where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element!
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True
            
            if toInsert:
                prev.next = Node(insertVal,curr)
                return head 
            
            # continue the loop until finish it 
            prev,curr = curr,curr.next 
            
            # loop finishes, return to the head and case 3 happens (n this case, we would end up looping through the list and getting back to the starting point.)
            if prev == head:
                break 
        
        # Case #3.
        # did not insert the node in the loop because loop contains the uniform value 
        prev.next = Node(insertVal, curr)
        return head 
       

# Time: O(N)
# Space:O(1)

