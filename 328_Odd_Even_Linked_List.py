# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # build two linked list for odd and even 
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        
        while head:
            odd.next = head 
            even.next = head.next 
            
            # move odd and even to next 
            odd = odd.next 
            even = even.next 
            
            # check if even is not None becaus even is always in ahead of odd
            if even:
                # start new head
                head = head.next.next 
            else:
                # stop the loop 
                head = None 
        
        # link odd and the first node of even (dummy2) together 
        odd.next = dummy2.next 
        return dummy1.next 

# Time: O(N)
# Space:O(1)