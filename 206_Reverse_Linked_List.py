# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None  
        cur = head 
        
        while cur:
            
        # switch current node with prev node 
            1->2: prev: None, 1: cur, 2: Next 
            Next = cur.next 
            # prev: none, 1->NULL
            cur.next = prev 
            
            # shift to the left:  
            # cur: 1, prev: none
            prev = cur
            
            # the most important to understand here:
            # Next:2,becomes to current node
            cur = Next
            
            # or: cur.next, prev, cur = prev, cur, cur.next
            # 3,1,2 = 1,2,3
        return prev 


# Time: O(N)
# Space:O(1)




# simpler code:
def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            
            # a,b,c = b,c,a, order: 4,5,6 = 1,2,3 
            # 1->2->3 => 3->2->1 
            cur.next, prev, cur = prev, cur, cur.next
        return prev

# other solution:

# recursion
# def reverseList(self, head):
#     return self._reverse(head)

# def _reverse(self, node, prev=None):
#     if not node:
#         return prev
#     n = node.next
#     node.next = prev
#     return self._reverse(n, node)

# Time: O(N)
# Space:O(N), The extra space comes from implicit stack space due to recursion. The recursion could go up to n levels deep.