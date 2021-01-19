# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

https://leetcode.com/problems/merge-k-sorted-lists/solution/

# Maybe follow up with 21.merge two sorted lists 
# we can directly add divide and conquer methd on merge 2 sorted lists 


# Approach 1: Brute Force
  # 1. Traverse all the linked lists and collect the values of the nodes into an array. 
  # 2.Sort and iterate over this array to get the proper value of nodes. 
  # 3.Create a new sorted linked list and extend it with the new nodes.
      
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        self.nodes = []
        dummy = ListNode(0)
        point = dummy 

        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next 
        
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next 
        return dummy.next 
    
    
# Time: O(NlogN)

# Collecting all the values costs O(N) time.
# A stable sorting algorithm costs O(NlogN) time.
# Iterating for creating the linked list costs O(N) time.

# Space:O(N)

# Sorting cost O(N) space (depends on the algorithm you choose).
# Creating a new linked list costs O(N) space.


# Approach 2: Compare one by one
# 1.Compare every k nodes (head of every linked list) and get the node with the smallest value.
# 2.Extend the final sorted linked list with the selected nodes.

# Time: O(NK)
# Space:O(N)



# Approach 3: optimize the comparison process by priority queue or heap 

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = cur = ListNode(None)
        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next

# Time: O(NlogK), where k is the number of linked lists.
# The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1) time.
# There are N nodes in the final linked list.

# Space:O(N)

# O(n) Creating a new linked list costs O(n) space.
# O(k) The code above present applies in-place method which cost O(1) space. And the priority queue (often implemented with heaps) costs O(k)O(k) space (it's far less than NN in most situations).


# Approach 4: merge one by one, Convert merge k lists problem to merge 2 lists (k-1) times. 

# Time: O(KN)

# We can merge two sorted linked list in O(n) time where nn is the total number of nodes in two lists
# Sum up the merge process and we can get: O(\sum_{i=1}^{k-1} (i*(\frac{N}{k}) + \frac{N}{k})) = O(kN)O(∑ 
# Space:O(1)

# We can merge two sorted linked list in O(1) space.



# Approach 5: merge with divide and conquer, the most optimum way.

# 1.Pair up k lists and merge each pair.
# 2.After the first pairing, k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.
# 3.Repeat this procedure until we get the final sorted linked list

# Thus, we'll traverse almost N nodes per pairing and merging, and repeat this procedure about  log_2 K times

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # The most optimum way is merge with divide and conquer: divide whole lists to pairs, for each pair, merge 2 sorted lists 
             
        # first solution
        lenK = len(lists)
        
        if lenK == 0:
            return None 
        
        interval = 1
        while interval < lenK:
            
            # mid = start + (end - start) // 2
            for i in range(0, lenK-interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0] 
        
        # second solution but will leads to runtime error 
#         if not lists:
#             return None
        
#         if len(lists) == 1:
#             return lists[0]
        
#         mid = len(lists) // 2
        
#         l = self.mergeKLists(lists[:mid])
#         r = self.mergeKLists(lists[mid:])
        
#         return self.merge2Lists(l, r)
    
    
    
    def merge2Lists(self,l1,l2):
        dummy = prev = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next 
            else:
                prev.next = l2
                l2 = l2.next 
            
            prev = prev.next 
        
        if l1:
            prev.next = l1
        
        if l2:
            prev.next = l2
        
        return dummy.next 
    


# Time: O(NlogK), where k is the number of linked lists.
# We can merge two sorted linked list in O(n) time where nn is the total number of nodes in two lists.
# Sum up the merge process and we can get: O(Nlogk)

# Space:O(1)
# We can merge two sorted linked lists in O(1) space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# V2: Recursion + Divide and Conquer  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return 
        
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists)//2
        
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        
        return self.merge2Lists(l,r)
        
        
    def merge2Lists(self,l1,l2):
        dummy = ListNode(0)
        prev = dummy 

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next 
            else:
                prev.next = l2
                l2 = l2.next 

            prev = prev.next 

        if l1:
            prev.next = l1

        if l2:
            prev.next = l2

        return dummy.next 
        
# Time: O(NlogK), k is the number of linked lists.
# Space:O(logK)
                
        
    
        







