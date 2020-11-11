# we can use stack to store value and pop but it is not constant space, O(N) linear space 
# we can also use recursion and it is same, still linear space, O(N)

# so instead we can create another node to switch with next until it reaches to the end 

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        
        # create two nodes
        # tail is the end pointer 
        # cur is to scan from head to tail 
        tail = None 
        cur = head
        
        # go from back to force 
        while tail!= head:
            while cur.getNext()!= tail:
                cur = cur.getNext()
            
            # reach to the None, which is the end
            # give tail the cur
            # then cur from head to scan it again 
            cur.printValue()
            tail = cur
            cur = head 
            
# Time: O(N)
# Space:O(1)


# Recursion 
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        # or we can use list []
        stack = deque([])
        stack.append(head)
        while head is not None:
            head = head.getNext()
            if head is not None:
                stack.append(head)
        while stack:
            stack.pop().printValue()

# Time: O(N)
# Space:O(N)
