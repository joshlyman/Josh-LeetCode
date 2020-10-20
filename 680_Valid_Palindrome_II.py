class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 1. brute force: to remove each single character to see if the resulting is a palindrome, O(n^2)
        
        # 2. greedy approach: if s[i] == s[j] then we take i++, j--, o.w. must be either s[i+1].. s[j] or s[i]..s[j-1], because we can have at most 1 char not to be inside palindrome 
        
        left,right = 0,len(s)-1
        
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                subarray1 = s[:left]+s[left+1:]
                subarray2 = s[:right]+s[right+1:]
                
                # [::-1] means flip the string, if flip still equal that means palindrome 
                return subarray1 == subarray1[::-1] or subarray2 == subarray2[::-1]
        
        # if all matches, no need to delete char 
        return True 
        
# Time: O(N)
# Space:O(1)