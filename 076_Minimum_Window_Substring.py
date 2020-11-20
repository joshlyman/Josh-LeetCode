
# Other solution
# V2

def minWindow(s, t):
    need = collections.Counter(t)            #hash table to store char frequency
    missing = len(t)                         #total number of chars we care
    start, end = 0, 0
    i = 0
    for j, char in enumerate(s, 1):          #index j from 1
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        if missing == 0:                     #match all chars
            while i < j and need[s[i]] < 0:  #remove chars to find the real start
                need[s[i]] += 1
                i += 1
            need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
            missing += 1                     #we missed this first char, so add missing by 1
            if end == 0 or j-i < end-start:  #update window
                start, end = i, j
            i += 1                           #update i to start+1 for next window
    return s[start:end]

# Time: O(|S|+|T|)
# Space:O(|S|+|T|)

# Refer from:
# https://leetcode.com/problems/minimum-window-substring/solution/


# Sliding Window 

# We start with two pointers, leftleft and rightright initially pointing to the first element of the string S.
# We use the rightright pointer to expand the window until we get a desirable window i.e. a window that contains all of the characters of T.
# Once we have a window with all the characters, we can move the left pointer ahead one by one. If the window is still a desirable one we keep on updating the minimum window size.
# If the window is not desirable any more, we repeat step 2 onwards.


# The current window is s[i:j] and the result window is s[I:J]. In need[c] I store how many times I 
# need character c (can be negative) and missing tells how many characters are still missing. 
# In the loop, first add the new character to the window. Then, if nothing is missing, 
# remove as much as possible from the window start and then update the result.

class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        m = len(s)
        n = len(t)
        if m < n:
            return ''
        lt = {}
        
        # put t into dict (lt) and count how many # for each char 
        for i in t:
            if i not in lt:
                lt[i] = 1
            else:
                lt[i] += 1
        
        # missing is to count how many remaining char needed from substring
        # finally get candidate substring which satisfy need of t 
        missing = n
        i = I = J = 0
        for j, c in enumerate(s, 1):    
            if c in lt and lt[c] > 0:
                missing -= 1
            if c in lt:
                # lt can be negative 
                lt[c] -= 1
            
            # i is index of candidate substring, remove as many as char from candidate
            while i < j and not missing:
                if not J or j-i < J-I:
                    I, J = i, j
                if s[i] not in lt:
                    i += 1
                    continue
                else:
                # if lt contains s[i], then # of s[i] +1, might reach to 0   
                    lt[s[i]] += 1
                    
                    # if > 0, means we need more, then missing +1 
                    if lt[s[i]] > 0:
                        missing += 1
                    i += 1
        return s[I:J]

# Time: O(|S|+|T|)
# Space:O(|S|+|T|)



# Optimized Sliding Window 

# A small improvement to the above approach can reduce the time complexity of the algorithm to O(2*∣filtered_S∣+∣S∣+∣T∣), 
# where filtered(S) is the string formed from S by removing all the elements not present in T


