# Two Pointers 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        spt = 0
        tpt = 0
        while spt < len(s) and tpt <len(t):
            if s[spt] == t[tpt]:
                spt+=1
            tpt+=1
        return spt == len(s)
        
# Time: O(|T|), Let∣S∣ be the length of the source string, and ∣T∣ be the length of the target string.
# Space:O(1)


# Other solution:
# https://leetcode.com/problems/is-subsequence/solution/