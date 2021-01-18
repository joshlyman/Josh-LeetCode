# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        
        if l2 == None:
            return l1
        
        
        dummy = ListNode(0)
        curr = dummy       
        carry = 0
        
        while l1 or l2:
            val = carry
            
            if l1:
                val +=l1.val
                l1 = l1.next 
            if l2:
                val += l2.val
                l2 = l2.next 
            
            carry,val = divmod(val,10)
            curr.next = ListNode(val)
            curr = curr.next 
            
        if carry == 1:
            curr.next = ListNode(1)
        
        return dummy.next


# V2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1:
            return l2
        
        if not l2:
            return l1
                    
        carry = 0
        dummy = ListNode(0)
        cur = dummy 
        
        while l1 or l2:
            
            val = carry  
            
            if l1:
                val += l1.val     
                l1 = l1.next 
            
            if l2:
                val += l2.val 
                l2 = l2.next 
            
            carry,val = val//10, val%10 
            cur.next = ListNode(val)
            cur = cur.next 
        
        # edge case: remain 1
        if carry:
            cur.next = ListNode(carry)
            
        return dummy.next 