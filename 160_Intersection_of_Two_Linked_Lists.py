# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# use two pointers to iterative A and B, then when in the end, switch A and B
# make A pointer start from B and B pointer starts from A
# in the end, they will meet because len(A)+len(B), which is same with method of fast and slow pointers 

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None 
        
        Apter = headA
        Bpter = headB
        
        while Apter !=Bpter:
            if Apter is None:
                Apter = headB
            else:
                Apter = Apter.next 
            
            if Bpter is None:
                Bpter = headA
            else:
                Bpter = Bpter.next 
                
        return Apter

# Time: O(M+N)
# Space:O(1)