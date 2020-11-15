# If we can not reverse our original lists, why not to put them into stack? So, what we do is the following:

# Iterate over the first and the second lists and create two stacks: st1 and st2.
# Iterate over stacks, pop last elements from stack if possible, if not, use 0 for empty stack. Add these two numbers and evaluate next digit and carry. Create new node with digit and attach it before current head, update head.
# Just return head in the end

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
            
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        
        carry, head = 0, None

        while st1 or st2 or carry:
            d1, d2 = 0, 0
            d1 = st1.pop() if st1 else 0
            d2 = st2.pop() if st2 else 0
            carry, digit = divmod(d1 + d2 + carry, 10)
            head_new = ListNode(digit)
            head_new.next = head
            # move head left 
            head = head_new
              
        return head

# Time: O(N)
# Space:O(N)