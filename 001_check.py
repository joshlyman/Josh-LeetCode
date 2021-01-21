Add Two Numbers 

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1:
            return l2
        
        if not l2:
            return l1
                    
        carry = 0
        dummy = ListNode(0)
        cur = dummy 
        
        while l1 or l2:
            
            val = carry  
            
            if l1:
                val += l1.val     
                l1 = l1.next 
            
            if l2:
                val += l2.val 
                l2 = l2.next 
            
            carry,val = val//10, val%10 
            cur.next = ListNode(val)
            cur = cur.next 
        
        # edge case: remain 1
        if carry:
            cur.next = ListNode(carry)
            
        return dummy.next


LRU Cache

# OrderedDict combines both hashmap and linked list

# 1. Get the key / Check if the key exists, move to the end 
# 2. Put the key
# 3. Delete the first added key (early key)

# get and put: in O(1) time are provided by the standard hashmap.  
# delete: O(1) in linked list.

# 1. OrderedDict
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:

            # return least used item (not return last item)
            self.popitem(last = False)

# Time:  O(1)
# both for put and get since all operations with ordered dictionary : get/in/set/move_to_end/popitem 
# (get/containsKey/put/remove) are done in a constant time.

# Space: O(capacity) since the space is used only for an ordered dictionary with at most capacity + 1 elements.


Next Permutation

# 1　　2　　7　　4　　3　　1   find 2 -> first element which is smaller that next element 

# 1　　2　　7　　4　　3　　1   find 3 -> smallest emlement which is larget that 2

# 1　　3　　7　　4　　2　　1   swap 2 and 3

# 1　　3　　[1　　2　　4　　7]   sort nums after 3


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        
        # from end to begining, find the earliest decreasing number, this number is in i-1, so k = i-1, kth number 
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        # nums are in descending order, has reached to the begining 
        if i == 0:   
            nums.reverse()
            return 
        
        # find the last ascending number, this number is in jth 
        k = i - 1    
        while nums[j] <= nums[k]:
            j -= 1
        
        # reverse these 2 numbers 
        nums[k], nums[j] = nums[j], nums[k]  
        
        # reverse the second part (from end to the first number, center is the second number)
        l, r = k+1, len(nums)-1  
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 
            r -= 1


Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:    
    
    # DFS / Backtracking
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
    
# Time: O(NxN!)
# Space: O(N!)



Reverse Linked List 

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None  
        cur = head 
        
        while cur:
            
        # switch current node with prev node 
            1->2: prev: None, 1: cur, 2: Next 
            Next = cur.next 
            # prev: none, 1->NULL
            cur.next = prev 
            
            # shift to the left:  
            # cur: 1, prev: none
            prev = cur
            
            # the most important to understand here:
            # Next:2,becomes to current node
            cur = Next
            
            # or: cur.next, prev, cur = prev, cur, cur.next
            # 3,1,2 = 1,2,3
        return prev 


# Time: O(N)
# Space:O(1)
