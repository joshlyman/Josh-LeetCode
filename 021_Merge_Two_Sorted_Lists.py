# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        
        prev = dummy 
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next 
            else:
                prev.next = l2
                l2 = l2.next 
            prev = prev.next 
        
        if l1 is not None:
            prev.next = l1
        else:
            prev.next = l2
        
        return dummy.next 

# Time: O(n+m)
# Space:O(n+m) 