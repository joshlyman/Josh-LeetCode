class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        PsudoNode = ListNode(0)
        PsudoNode.next = head
        
        prev,curr = PsudoNode,head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next 
            else:
                prev = curr
            curr = curr.next 
        
        return PsudoNode.next 

# Time: O(N)
# Space:O(1)