# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Iteration 
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
# Space:O(1)


# Recursion 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        
# Time: O(n+m)
# Space:O(n+m)            