# iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        prev = None
        curr = head
        
        while curr:
            nex = curr.next 
            curr.next = prev
            prev = curr 
            curr = nex 
        
        return prev 

# Time: O(N)
# Space:O(1)


# simpler code:
def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            
            # a,b,c = b,c,a, order: 4,5,6 = 1,2,3 
            # 1->2->3 => 3->2->1 
            cur.next, prev, cur = prev, cur, cur.next
        return prev

# other solution:

# recursion
# def reverseList(self, head):
#     return self._reverse(head)

# def _reverse(self, node, prev=None):
#     if not node:
#         return prev
#     n = node.next
#     node.next = prev
#     return self._reverse(n, node)

# Time: O(N)
# Space:O(N), The extra space comes from implicit stack space due to recursion. The recursion could go up to n levels deep.