# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head 
        
        # This problem is to remove L-N+1 th node from list, it is easy to solve once we found list length L. Then we move the pointer until it reaches L-N th node and we link the L-N th node with L-N+2 th node. 
        
        first = head 
        length = 0

        # if first is not NULL 
        while first:
            length+=1
            first = first.next 
        
        # move pointer to L-N th node 
        length -=n 
        second = dummy
        
        while length >0:
            length-=1
            second = second.next 
        
        # link L-N th node with L-N+2 th node 
        second.next = second.next.next 
        
        return dummy.next 
        

# Time: O(L)
# Space:O(1)      
        
        
# V2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head 
        
        first = head 
        length = 0
        
        while first:
            first = first.next 
            length +=1
                
        length = length -n
        second = dummy 
        
        while length>0:
            second = second.next 
            length -=1
        
        second.next = second.next.next 
        
        return dummy.next 
             
        