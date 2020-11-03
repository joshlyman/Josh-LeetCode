# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Official solution:
# https://leetcode.com/problems/sort-list/solution/
# Details on merge sort is inside 

# Merge Sort 
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start = slow.next
        slow.next = None
        l, r = self.sortList(head), self.sortList(start)
        return self.merge(l, r)
        
        
    def merge(self, l, r):
        if not l or not r:
            return l or r
        dummy = p = ListNode(0)
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next

# Time: O(NlogN), where nn is the number of nodes in linked list. The algorithm can be split into 2 phases, Split and Merge.


# Space:O(logN)
# where nn is the number of nodes in linked list. Since the problem is recursive, we need additional space 
# to store the recursive call stack. The maximum depth of the recursion tree is nlogn

# quick sort 

# Quicksort is also one of the efficient algorithms with the average time complexity of 
# O(nlogn). But the worst-case time complexity is O(n^2). Also, variations of the quick sort 
# like randomized quicksort are not efficient for the linked list because unlike arrays, 
# random access in the linked list is not possible in O(1) time. If we sort the linked list 
# using quicksort, we would end up using the head as a pivot element which may not be efficient in all scenarios.

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def partition(start, end):
            node = start.next.next
            pivotPrev = start.next
            pivotPrev.next = end
            pivotPost = pivotPrev
            while node != end:
                temp = node.next
                if node.val > pivotPrev.val:
                    node.next = pivotPost.next
                    pivotPost.next = node
                elif node.val < pivotPrev.val:
                    node.next = start.next
                    start.next = node
                else:
                    node.next = pivotPost.next
                    pivotPost.next = node
                    pivotPost = pivotPost.next
                node = temp
            return [pivotPrev, pivotPost]
        
        def quicksort(start, end):
            if start.next != end:
                prev, post = partition(start, end)
                quicksort(start, prev)
                quicksort(post, end)

        newHead = ListNode(0)
        newHead.next = head
        quicksort(newHead, None)
        return newHead.next

# Time: best is O(NlogN), worst is O(N^2)
# Space: O(1)