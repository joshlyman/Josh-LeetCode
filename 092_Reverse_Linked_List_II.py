# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        
        cur,prev = head,None
        
        while m >1:
            prev = cur
            cur = cur.next 
            m,n = m-1,n-1
        
        tail,con = cur,prev
        
        # 1->2->3 prev-> cur->cur.next 
        # 3->2->1 cur ->prev -> prev.next 
        while n:
            nex = cur.next # nex: 3
            cur.next = prev # cur.next: 1
            prev = cur# prev:2
            cur = nex# cur:3
            n-=1 
        
        if con:
            con.next = prev
        else:
            head = prev 
        
        tail.next = cur 
        
        return head 
        
        
        
# Time: O(m+n)
# Space:O(1)