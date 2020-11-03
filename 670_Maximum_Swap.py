
# Brute force is to find all possible options: C_N_2 then compare each one to find the maxi

# Afterwards, when scanning the number from left to right, if there is a larger digit in the future, we will swap it 
# with the largest such digit; if there are multiple such digits, we will swap it with the one that occurs the latest.

# One pass 
# Basic idea:
# Find a index i, where there is a increasing order
# On the right side of i, find the max value (max_val) and its index (max_idx)
# On the left side of i, find the most left value and its index (left_idx), which is less than max_val
# Swap above left_idx and max_idx if necessary

class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        for i in range(n-1):                                # find index where s[i] < s[i+1], meaning a chance to flip
            if s[i] < s[i+1]: 
                break
        else: 
            return num                                    # if nothing find, return num
        max_idx, max_val = i+1, s[i+1]                      # keep going right, find the maximum value index
        for j in range(i+1, n):
            if max_val <= s[j]: 
                max_idx, max_val = j, s[j]                                       # going right from i, find most left value that is less than max_val
        for j in range(i, -1, -1):    
            if s[j] < max_val: 
                left_idx = j
        s[max_idx], s[left_idx] = s[left_idx], s[max_idx]   # swap maximum after i and most left less than max
        return int(''.join(s))                              # re-create the integer

# Time: O(N)
# Space:O(1)


