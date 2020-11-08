# A binary search tree is essentially a rooted binary tree with a very special property or relationship amongst its nodes. 
# For a given node of the binary search tree, it's value must be \ge≥ the value of all the nodes in the left subtree and <= 
# the value of all the nodes in the right subtree. Since a binary tree has a recursive substructure, so does a BST i.e.
# all the subtrees are binary search trees in themselves.

# Main Idea: 
# the middle element of the given list would form the root of the binary search tree. 
# All the elements to the left of the middle element would form the left subtree recursively. 
# Similarly, all the elements to the right of the middle element will form the right subtree of the binary 
# search tree. This would ensure the height balance required in the resulting binary search tree.


# offical Solution:
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solution/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 1.Use fast and slow pointers to do recursion 

# 1.Since we are given a linked list and not an array, we don't really have access to the elements of the list using indexes. 
# We want to know the middle element of the linked list.

# 2.We can use the two pointer approach for finding out the middle element of a linked list. Essentially, 
# we have two pointers called slow_ptr and fast_ptr. The slow_ptr moves one node at a time whereas the 
# fast_ptr moves two nodes at a time. By the time the fast_ptr reaches the end of the linked list, the 
# slow_ptr would have reached the middle element of the linked list. For an even sized list, any of the 
# two middle elements can act as the root of the BST.

# 3.Once we have the middle element of the linked list, we disconnect the portion of the list to the left 
# of the middle element. The way we do this is by keeping a prev_ptr as well which points to one node before 
# the slow_ptr i.e. prev_ptr.next = slow_ptr. For disconnecting the left portion we simply do prev_ptr.next = None
# We only need to pass the head of the linked list to the function that converts it to a height balances BST. 
# So, we recurse on the left half of the linked list by passing the original head of the list and on the right 
# half by passing slow_ptr.next as the head.

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return 
        
        if not head.next:
            return TreeNode(head.val)
        # here we get the middle point,
        # even case, like '1234', slow points to '2',
        # '3' is root, '12' belongs to left, '4' is right
        # odd case, like '12345', slow points to '2', '12'
        # belongs to left, '3' is root, '45' belongs to right
        
        # Use slow and fast two pointers to get the middle point 
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # tmp points to root, this is middle point for root 
        tmp = slow.next
        
        # cut down the left child
        slow.next = None
        root = TreeNode(tmp.val)
        
        # build left subtree: from head to slow (slow.next is None)
        root.left = self.sortedListToBST(head)
        # build right subtree: from mid (tmp.next) to end 
        root.right = self.sortedListToBST(tmp.next)
        return root

# Time: O(NlogN)
# Space:O(logN)


# 2. Recursion + Conversion to Array

# We can get the time complexity down by using more space.

# Convert the given linked list into an array. Let's call the beginning and the end of the array as left and right
# Find the middle element as (left + right) / 2. Let's call this element as mid. This is a O(1) time operation and is the 
# only major improvement over the previous algorithm.
# The middle element forms the root of the BST.
# Recursively form binary search trees on the two halves of the array represented by (left, mid - 1) and (mid + 1, right) respectively.


class Solution:

    # Convert the given linked list to an array
    def mapListToValues(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals    

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # Form an array out of the given linked list and then
        # use the array to form the BST.
        values = self.mapListToValues(head)

        # l and r represent the start and end of the given array
        def convertListToBST(l, r):

            # Invalid case
            if l > r:
                return None

            # Middle element forms the root.
            mid = (l + r) // 2
            node = TreeNode(values[mid])

            # Base case for when there is only one element left in the array
            if l == r:
                return node

            # Recursively form BST on the two halves
            node.left = convertListToBST(l, mid - 1)
            node.right = convertListToBST(mid + 1, r)
            return node
        return convertListToBST(0, len(values) - 1)

# Time: O(N)

# The time complexity comes down to just O(N) now since we convert the linked list to an array initially and 
# then we convert the array into a BST. Accessing the middle element now takes O(1) time and hence the time 
# complexity comes down.

# Space:O(N)

# Since we used extra space to bring down the time complexity, the space complexity now goes up to O(N) as opposed 
# to just O(logN) in the previous solution. This is due to the array we construct initially.



# 3.Inorder Simulation

# Elements processed in the inorder fashion on a binary search tree turn out to be sorted in ascending order.

# The approach listed here make use of this idea to formulate the construction of a binary search tree. 
# The reason we are able to use this idea in this problem is because we are given a sorted linked list initially.

# We know that the leftmost element in the inorder traversal has to be the head of our given linked list. 
# Similarly, the next element in the inorder traversal will be the second element in the linked list and so on. 
# This is made possible because the initial list given to us is sorted in ascending order.

# 1.Iterate over the linked list to find out it's length. We will make use of two different pointer variables here to mark the 
# beginning and the end of the list. Let's call them start and end with their initial values being 0 and length - 1 respectively.

# 2.Remember, we have to simulate the inorder traversal here. We can find out the middle element by using (start + end) / 2. 
# Note that we don't really find out the middle node of the linked list. We just have a variable telling us the index of the 
# middle element. We simply need this to make recursive calls on the two halves.

# 3.Recurse on the left half by using start, mid - 1 as the starting and ending points.

# 4.The invariance that we maintain in this algorithm is that whenever we are done building the left half of the BST, 
# the head pointer in the linked list will point to the root node or the middle node (which becomes the root). 
# So, we simply use the current value pointed to by head as the root node and progress the head node by once i.e. head = head.next

# 5.We recurse on the right hand side using mid + 1, end as the starting and ending points.


class Solution:

    def findSize(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # Get the size of the linked list first
        size = self.findSize(head)

        # Recursively form a BST out of linked list from l --> r
        def convert(l, r):
            nonlocal head

            # Invalid case
            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal. Recursively form
            # the left half
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node
            node = TreeNode(head.val)   
            node.left = left

            # Maintain the invariance mentioned in the algorithm
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node
        return convert(0, size - 1)

# Time: O(N), since we still have to process each of the nodes in the linked list once and form corresponding BST nodes.

# Space:O(logN) since now the only extra space is used by the recursion stack and since we are 
# building a height balanced BST, the height is bounded by logN.









