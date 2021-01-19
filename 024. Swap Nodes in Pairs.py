# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursion
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head 
        
        first_node = head
        second_node = head.next 
        
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node 
        
        return second_node

# Time: O(N)
# Space:O(N)


# Iterative 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next

# Time: O(N)
# Space:O(1)


# V2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head 
        
#         first,second = head,head.next 
        
#         first.next = self.swapPairs(second.next)
#         second.next = first 
        
#         return second 

        dummy = ListNode(0)
        dummy.next = head 
        prev = dummy 
        
        while head and head.next:
            first,second = head,head.next 
            
            # swap nodes
            # 0->2
            prev.next = second 
            # 1->3
            first.next = second.next 
            # 2->1
            second.next = first 
            
            # prev is now 2 
            prev = first 
            # start from 3
            head = first.next 
            
        return dummy.next
            
    
    
    
        
        