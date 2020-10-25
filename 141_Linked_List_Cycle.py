# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # we can use hash table to store each node and check if it cotains again. if contains then it is True, ow, it is false, requires O(N) for space 
        
        # use two pointers with fast and slow speed and check if they can meet again. 
        # space is O(1)
        
        if head is None:
            return False 
        
        # fast and slow cannot start from same position 
        fast = head.next 
        slow = head 
        
        while fast!= slow:
            if fast == None or fast.next == None:
                return False
            
            slow = slow.next 
            fast = fast.next.next 
        
        return True 
        
# Time: O(N)
# Space:O(1)