# Definition for a  binary tree node

# refer from: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/35223/An-easy-Python-solution 

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    # 12:37
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root

# Time: O(NLogN)
# Space:O(N) as the maximum length of the stack is N.


# refer from https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/264853/Python-3-recursive-O(n)-solution-beats-82

# This might be nice and easy to code up, but the asymptotic complexity is bad. Slices take O(s) where 's' is the size of the slice.
# Therefore this algorithm has runtime O(n lg n), space O(n), wheras it could be done in O(n) runtime and O(lg n) space complexity if passing indices of the start and end of string instead of the slices directly.

# refer this picture on runtime O(n lg n): https://imgur.com/vZBVjUx 

# A lot of the Python solutions use slices to split the array; however, it takes O(n) to slice, making the entire algorithm O(n logn). 
# Therefore, we create a helper function to pass in the bounds of the array instead, making it O(n):

def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
	return self.helper(nums, 0, len(nums))

def helper(self, nums, lower, upper):
	if lower == upper:
		return None

	mid = (lower + upper) // 2
	node = TreeNode(nums[mid])
	node.left = self.helper(nums, lower, mid)
	node.right = self.helper(nums, mid+1, upper)

	return node

# Time: O(N)
# Space:O(logN) as the maximum length of the stack is log N.

