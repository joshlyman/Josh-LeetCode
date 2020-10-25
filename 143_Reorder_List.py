# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1.find a middle node using fast and slow two pointers
        # 2.reverse second part 
        # 3.merge first and second parts 
        
        
        if head is None: 
            return None 
        
        slow = fast = head 
        while fast and fast.next:
            # fast approches 2 steps, so slow is middle when fast goes to the end 
            slow = slow.next 
            fast = fast.next.next 
        
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev,curr = None,slow 
        while curr:
            curr.next,prev,curr = prev,curr,curr.next 
        
        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first,second = head,prev
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp

            tmp = second.next
            second.next = first
            second = tmp
        
        # another simple way:
        # first, second = head, prev
        # while second.next:
        #     first.next, first = second, first.next
        #     second.next, second = first, second.next
                
# Time: O(N)
# Space:O(1)