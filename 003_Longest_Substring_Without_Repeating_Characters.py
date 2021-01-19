# Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = -1
        max = 0

        # store element and its index 
        d = {}
        
        for i in range(len(s)):
            if s[i] in d and d[s[i]]>start:
                # reset the start index if meet same elements again 
                start = d[s[i]]
                d[s[i]] = i
            else:
                d[s[i]] = i
                if i - start > max:
                    max = i -start 
                    
        return max 

# time: O(n)
# space: O(n)
