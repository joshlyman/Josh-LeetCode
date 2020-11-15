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
# Space:O(N) because of additional memort from subarray 1 and 2


# my solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left,right = 0,len(s)-1
        
        while left< right:
            if s[left] == s[right]:
                left +=1
                right -=1
            else:
                # skip left or right element to compare remaining elements
                return self.helper(s, left +1,right) or self.helper(s,left,right-1)
        
        # must be careful here for those true example when done, for example, aba 
        return True 
        
    def helper(self,s,left,right):
        
        while left< right:
            if s[left] == s[right]:
                left +=1
                right -=1
            else:
                return False
        return True 

# Time: O(N)
# Space:O(1)