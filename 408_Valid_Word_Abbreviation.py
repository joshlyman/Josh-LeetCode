# We maintain two pointers, i pointing at word and j pointing at abbr.
# There are only two scenarios:

# j points to a letter. We compare the value i and j points to. If equal, we increment them. Otherwise, return False.
# j points to a digit. We need to find out the complete number that j is pointing to, e.g. 123. Then we would increment i by 123. We know that next we will:
# either break out of the while loop if i or j is too large
# or we will return to scenario 1.

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0 
        while j < len(abbr) and i < len(word): 
            if abbr[j].isalpha(): 
                if abbr[j] != word[i]: 
                    return False 
                # if abbr[j] == word[i]:
                i += 1 
                j += 1 
            else: 
                if abbr[j] == '0':  # to handle edge cases such as "01", which are invalid
                    return False 
                
                # if abbr[j] is digit then need to get # of digits between this alpha with next alpha  
                temp = 0 
                while j < len(abbr) and abbr[j].isdigit(): 
                    temp = temp * 10 + int(abbr[j]) 
                    j += 1 
                i += temp  
        
        # both reaches to the end 
        return j == len(abbr) and i == len(word)

# Time: O(Max(M,N))
# Space:O(1)