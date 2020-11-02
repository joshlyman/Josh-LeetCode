
# Approach 1: sliding window + Hashmap 

class Solution(object):
    
    """
    The general idea is to iterate over string s.
    Always put the character c and its location i in the dictionary d.
    1) If the sliding window contains less than or equal to k distinct characters, simply record the return value, and move on.
    2) Otherwise, we need to remove a character from the sliding window.
       Here's how to find the character to be removed:
       Because the values in d represents the rightmost location of each character in the sliding window, in order to find the longest substring T, we need to locate the smallest location, and remove it from the dictionary, and then record the return value.
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret

# Time: O(N)
# Space:O(K)


Other solution:
from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s) 
        if k == 0 or n == 0:
            return 0
        
        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position 
        # in the sliding window
        hashmap = defaultdict()

        max_len = 1
        
        while right < n:
            # add new character and move right pointer
            hashmap[s[right]] = right
            right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == k + 1:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len

# Time: O(N) in the best case of k distinct characters in the string and O(Nk) in 
# the worst case of N distinct characters in the string.

# For the best case when input string contains not more than k distinct characters the answer is yes. 
# It's the only one pass along the string with N characters and the time complexity is O(N).

# For the worst case when the input string contains n distinct characters, the answer is no. 
# In that case at each step one uses O(k) time to find a minimum value in the hashmap with 
# k elements and so the overall time complexity is O(Nk).



# Space:O(K) since additional space is used only for a hashmap with at most k + 1 elements.

# To achieve O(N) time 
# Approach 2: Sliding Window + Ordered Dictionary

# There is a structure called ordered dictionary, it combines behind both hashmap and linked list. 
# In Python this structure is called OrderedDict, which provides four operations in O(1) time: 
# Insert the key, Get the key / Check if the key exists / Delete the key / Return the first / or the last added key/value
# The first three operations in O(1) time are provided by the standard hashmap, 
# and the forth one - by linked list.

# So Only difference is that If ordered dictionary hashmap contains k + 1 distinct characters, 
# remove the leftmost one and move the left pointer so that sliding window 
# contains again k distinct characters only.

from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: 'str', k: 'int') -> 'int':
        n = len(s) 
        if k == 0 or n == 0:
            return 0
        
        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position 
        # in the sliding window
        hashmap = OrderedDict()

        max_len = 1
        
        while right < n:
            character = s[right]
            # if character is already in the hashmap -
            # delete it, so that after insert it becomes
            # the rightmost element in the hashmap
            if character in hashmap:
                del hashmap[character]
            hashmap[character] = right
            right += 1

            # slidewindow contains k + 1 characters
            if len(hashmap) == k + 1:
                # delete the leftmost character
                _, del_idx = hashmap.popitem(last = False)
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len

# Time: O(N) since all operations with ordered dictionary : 
# insert/get/delete/popitem (put/containsKey/remove) are done in a constant time.

# Space: O(k) since additional space is used only for an ordered dictionary 
# with at most k + 1 elements.







