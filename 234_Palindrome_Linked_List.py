# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next 
            
        # vals[::-1] is reverse of vals     
        return vals == vals[::-1]

# Time: O(N)
# Space:O(N)

